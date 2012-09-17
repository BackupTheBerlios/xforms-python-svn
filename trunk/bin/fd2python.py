#!/usr/bin/env python3
# -*- coding: iso8859-1 -*-

""" xforms-python's script to convert fdesign '.fd' files to python UI layout.
"""

#    Copyright (C) 2010, 2011  Luca Lazzaroni "LukenShiro"
#    e-mail: <lukenshiro@ngi.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, version 2.1 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU LGPL along with this
#    program. If not, see <http://www.gnu.org/licenses/>.
#
#    See CREDITS file to read acknowledgements and thanks to XForms,
#    ctypes and other developers.

import sys
import os
from xformslib import vers, xfstruct

# constants
ONETAB = "    "
TWOTABS = ONETAB * 2


def xfcopyright():
    message = 'xforms-python conversion script from fdesign .fd files to' \
            ' python UI layout\nIt is part of xforms-python version ' \
            '%s\nCopyright (C) 2010  Luca Lazzaroni "LukenShiro"\n' \
            'It is released under LGPL 2.1 license. See LICENSE file' \
            ' for details.\n' % vers.__version__
    print(message)

def errorcliargs(msg="", exval=0):
    xfcopyright()
    if exval > 0:
        message = "Fatal error: %s\n" % msg
        print(message)
    message = "Usage: fd2python.py <infile>.fd [<outfile>.py]\n" \
            "If <outfile>.py is omitted, <infile>.py is used\n" \
            "<outfile>.py should not be existing."
    print(message)
    sys.exit(exval)

def prependxfl(valuestr):
    if valuestr.startswith("FL_"):
        valuestr = valuestr.replace("FL_", "xfl.FL_")
    return valuestr

def prependself(valuestr):
    if valuestr:
        valuestr = "self."+valuestr
    return valuestr

def sanitize(valuestr):
    if valuestr:
        valuestr = valuestr.replace("'", "\'")
    return valuestr

def prependfltype(valuestr):
    # to be compatible with magic < 15000, prepend a FL_ to type
    if not valuestr.startswith("FL_"):
        valuestr = "FL_"+valuestr
    return valuestr


class FdConvertToPy(object):
    def __init__(self, lsysargv, sysargv):
        self.listpairsofelem = []    # list of elements' unmanaged pairs
        self.listdictsofelem = []    # list of elements' dicts

        self.nameflformlist = []     # name entries for form
        self.nameflgrouplist = []     # name entries for group
        self.nameflobjlist = []     # name entries for flobj

        self.headertext = []        # env python, header comment
        self.inittext = []      # import, class, fl_initialize
        self.maintext = []          # call to form creation defs
        self.endmaintext = []       # show form, fl_finish
        self.preformtext = []       # def createforms
        self.createformstext = []   # complete form creation defs
        self.callbacktext = []      # defs of callbacks funcs
        self.runcodetext = []           # if __name__ etc...

        self.numforms = 0
        self.numflobjs = 0

        self.formnum = 0        # progressive number for generic names
        self.groupnum = 0        # progressive number for generic names
        self.flobjnum = 0        # progressive number for generic names

        self.firstformname = ""
        self.isfirstform = True
        self.nameofflobject = ""

        self.infile = ""
        self.outfile = ""

        if self.cliargs(lsysargv, sysargv):
            self.appname = self.infile.replace(".fd", \
                    "").replace("/", "_").replace("-", "_").capitalize()
            if self.verifyfdfile():
                self.acquirechunks()
                self.convertlistsindict()
                self.analysedictelems()
                self.savepyfile()

    def cliargs(self, lsysargv, sysargv):
        # manage cli args
        if lsysargv == 3:       # infile.fd and outfile.py passed
            if not os.path.exists(sysargv[1]) or \
                    not sysargv[1].endswith(".fd"):
                # infile.fd not existent
                errorcliargs('<infile>.fd must exist', 1)
            if os.path.exists(sysargv[2]):         # outfile.py existent
                errorcliargs('<outfile>.py must NOT exist', 2)
            self.infile = sysargv[1]
            self.outfile = sysargv[2]
            return True
        elif lsysargv == 2:     # infile.fd passed only
            if not os.path.exists(sysargv[1]) or \
                    not sysargv[1].endswith(".fd"):
                # infile.fd not existent
                errorcliargs('<infile>.fd must exist', 1)
            self.infile = sysargv[1]
            self.outfile = sysargv[1].replace('.fd', '.py')
            if os.path.exists(self.outfile):         # outfile.py existent
                errorcliargs('<outfile>.py must NOT exist', 2)
            return True
        else:
            errorcliargs('Wrong number of arguments passed.', 3)

    def verifyfdfile(self):
        # open .fd
        fdin = open(self.infile, 'r')
        # verify if it is .fd compliant format
        initialtxt = fdin.read(100)
        fdin.close()
        if not "Internal Form Definition File" in initialtxt:
            errorcliargs('<infile>.fd is not in correct .fd format.', 4)
        else:
            return True

    def acquirechunks(self):
        # read and organize in list of strings all chunks of data
        fdin = open(self.infile, 'r')
        numlines = sum(1 for line in fdin)
        fdin.close()
        self.listpairsofelem = [""] * numlines
        thereisform = False
        thereisflobj = False

        fdin = open(self.infile, 'r')
        elemnum = 0
        for line in fdin:
            if line.startswith('Magic') or 'Internal Form' in line or \
                    line.startswith('\n'):    # lines to ignore
                continue
            elif "do not change" in line:          # new intro
                self.listpairsofelem[elemnum] = "<INTRO>", None
                elemnum += 1
                self.listpairsofelem[elemnum] = []
            elif "== FORM ==" in line:          # new form
                if thereisform:     # a form is already present
                    self.listpairsofelem[elemnum] = "<ENDFORM>", None
                    elemnum += 1
                else:                    # intro before this one
                    self.listpairsofelem[elemnum] = "<ENDINTRO>", None
                    elemnum += 1
                self.listpairsofelem[elemnum] = "<FORM>", None
                elemnum += 1
                self.listpairsofelem[elemnum] = []
                thereisform = True
            elif line.startswith('------'):   # new flobject
                if thereisflobj:     # a flobj is already present
                    self.listpairsofelem[elemnum] = "<ENDFLOBJ>", None
                    elemnum += 1
                elif thereisform:    # first flobj in the form
                    self.listpairsofelem[elemnum] = "<ENDFORMHEAD>", None
                    elemnum += 1
                self.listpairsofelem[elemnum] = "<FLOBJ>", None
                elemnum += 1
                self.listpairsofelem[elemnum] = []
                thereisflobj = True
            elif "==============================" in line:      # EOF
                self.listpairsofelem[elemnum] = "<ENDFLOBJ>", None
                elemnum += 1
                self.listpairsofelem[elemnum] = "<ENDALL>", None
                elemnum += 1
                break
            else:
                linenew = line.strip()
                npos = linenew.find(":")
                if npos == -1:          # ':' not found
                    continue
                else:                   # first ':' is the border
                    mykey = (linenew[:npos]).strip()
                    myvalue = (linenew[npos+1:]).strip()
                    if not myvalue:     # not a value (placeholder)
                        myvalue = None
                self.listpairsofelem[elemnum] = mykey, myvalue
                elemnum += 1
        fdin.close()

    def convertlistsindict(self):
        # organize key-value pairs in dict
        self.listdictsofelem = []   #* (len(self.listpairsofelem)/2)

        unitold = 0     # a key-value pair of old list
        unitnew = 0     # a block belonging to intro or form header or flobj
        singdict = ""
        while True:
            elem = self.listpairsofelem[unitold]
            if elem[0] == "<INTRO>":
                del singdict
                singdict = {'phase' : 'INTRO'}
                unitold += 1
            elif elem[0] == "<ENDINTRO>":
                self.listdictsofelem.append(singdict)
                #del singdict
                unitold += 1
                unitnew += 1
            elif elem[0] == "<FORM>":
                del singdict
                singdict = {'phase' : 'FORM'}
                unitold += 1
            elif elem[0] == "<ENDFORMHEAD>":
                self.listdictsofelem.append(singdict)
                unitold += 1
                unitnew += 1
            elif elem[0] == "<FLOBJ>":
                del singdict
                singdict = {'phase' : 'FLOBJ'}
                unitold += 1
            elif elem[0] == "<ENDFLOBJ>":
                self.listdictsofelem.append(singdict)
                unitold += 1
                unitnew += 1
            elif elem[0] == "<ENDALL>":
                del singdict
                singdict = {'phase' : 'ENDFORM'}
                self.listdictsofelem.append(singdict)
                break
            elif elem[0] == "<ENDFORM>":
                del singdict
                singdict = {'phase' : 'ENDFORM'}
                self.listdictsofelem.append(singdict)
                unitold += 1            # next
                unitnew += 1
            else:               # real key-value pair
                if isinstance(singdict, dict):
                    mykey = elem[0]
                    myval = elem[1]
                    singdict[mykey] = myval
                    unitold += 1

    def analysedictelems(self):
        # calls appropriate routines to manage macrounit
        self.manage_header()
        for macrounit in self.listdictsofelem:
            if macrounit['phase'] == 'INTRO':
                self.manage_intro(macrounit)
                self.manage_preform()
            elif macrounit['phase'] == 'FORM':
                self.manage_flbeginform(macrounit)
            elif macrounit['phase'] == 'ENDFORM':
                self.manage_flendform()
            elif macrounit['phase'] == 'FLOBJ':
                if macrounit['class'] == 'FL_BEGIN_GROUP':
                    myname = self.manage_flbegingroup(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_END_GROUP':
                    self.manage_flendgroup()
                elif macrounit['class'] == 'FL_BITMAP':
                    myname = self.manage_flbitmap(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_BITMAPBUTTON':
                    myname = self.manage_flbitmapbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_BOX':
                    myname = self.manage_flbox(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_BROWSER':
                    myname = self.manage_flbrowser(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_BUTTON':
                    myname = self.manage_flbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_CANVAS':
                    myname = self.manage_flcanvas(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_CHART':
                    myname = self.manage_flchart(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_CHECKBUTTON':
                    myname = self.manage_flcheckbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_CLOCK':
                    myname = self.manage_flclock(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_COUNTER':
                    myname = self.manage_flcounter(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_DIAL':
                    myname = self.manage_fldial(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_FORMBROWSER':
                    myname = self.manage_flformbrowser(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_FRAME':
                    myname = self.manage_flframe(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_FREE':
                    myname = self.manage_flfree(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_GLCANVAS':
                    myname = self.manage_flglcanvas(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_INPUT':
                    myname = self.manage_flinput(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_LABELBUTTON':
                    myname = self.manage_fllabelbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_LABELFRAME':
                    myname = self.manage_fllabelframe(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_LIGHTBUTTON':
                    myname = self.manage_fllightbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_PIXMAP':
                    myname = self.manage_flpixmap(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_PIXMAPBUTTON':
                    myname = self.manage_flpixmapbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_POSITIONER':
                    myname = self.manage_flpositioner(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_ROUND3DBUTTON':
                    myname = self.manage_flround3dbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_ROUNDBUTTON':
                    myname = self.manage_flroundbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_SCROLLBAR':
                    myname = self.manage_flscrollbar(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_SCROLLBUTTON':
                    myname = self.manage_flscrollbutton(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_SLIDER':
                    myname = self.manage_flslider(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_SPINNER':
                    myname = self.manage_flspinner(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_TABFOLDER':
                    myname = self.manage_fltabfolder(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_TEXT':
                    myname = self.manage_fltext(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_TIMER':
                    myname = self.manage_fltimer(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_THUMBWHEEL':
                    myname = self.manage_flthumbwheel(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_VALSLIDER':
                    myname = self.manage_flvalslider(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_XYPLOT':
                    myname = self.manage_flxyplot(macrounit)
                    self.manage_genericflobject(macrounit, myname)
                elif macrounit['class'] == 'FL_CHOICE':
                    print("FL_CHOICE flobject is deprecated, it will be" \
                            " ignored.")
                elif macrounit['class'] == 'FL_MENU':
                    print("FL_MENU flobject is deprecated, it will be " \
                            "ignored.")
        self.manage_endmain()
        self.manage_endings()

    def getgeneric_flformname(self):
        nameflform = "ptrflform%s" % str(self.formnum)
        while nameflform in self.nameflformlist:
            self.formnum += 1
            nameflform = "ptrflform%s" % str(self.formnum)
        self.nameflformlist.append(nameflform)
        return nameflform

    def getgeneric_flgroupname(self):
        nameflgroup = "ptrgroup%s" % str(self.groupnum)
        while nameflgroup in self.nameflgrouplist:
            self.groupnum += 1
            nameflgroup = "ptrgroup%s" % str(self.groupnum)
        self.nameflgrouplist.append(nameflgroup)
        return nameflgroup

    def getgeneric_flobjname(self):
        nameflobj = "ptrflobj%s" % str(self.flobjnum)
        while nameflobj in self.nameflobjlist:
            self.flobjnum += 1
            nameflobj = "ptrflobj%s" % str(self.flobjnum)
        self.nameflobjlist.append(nameflobj)
        return nameflobj

    def manage_header(self):
        headtxt = "#!/usr/bin/env python\n# Forms definition originally " \
                "created with XForms fdesign.\n# Converted by fd2python.py" \
                " to be used with xforms-python.\n"
        self.headertext.append(headtxt)
        introtxt = "\nimport sys"
        introtxt += "\nimport xformslib as xfl"
        introtxt += "\n\nclass %s(object):" % self.appname
        introtxt += "\n%sdef __init__(self, lsysargv, sysargv):" % ONETAB
        introtxt += "\n%sxfl.fl_initialize(lsysargv, sysargv, '%s', " \
                "None, 0)\n" % (TWOTABS, self.appname)
        self.inittext.append(introtxt)

    def manage_intro(self, macrounit):
        # INTRO area
        introtxt = ""
        if "Number of forms" in macrounit:
            self.numforms = macrounit["Number of forms"]
        if "Unit of measure" in macrounit:
            value = macrounit['Unit of measure']
            introtxt = "\n%sxfl.fl_set_coordunit(%s)" % \
                    (TWOTABS, prependxfl(value))
        if "Border Width" in macrounit:
            value = macrounit['Border Width']
            introtxt = "\n%sxfl.fl_set_border_width(%s)" % (TWOTABS, value)
        self.inittext.append(introtxt)

    def manage_preform(self):
        preform = "\n\n%sdef create_forms(self):" % ONETAB
        self.preformtext.append(preform)

    def manage_flbeginform(self, macrounit):
        # FORM area
        formtxt = ""
        if "Number of Objects" in macrounit:    # unused here currently
            self.numflobjs = macrounit['Number of Objects']
        if "Name" in macrounit:
            if macrounit['Name'] is None:       # name unknown
                vname = self.getgeneric_flformname()
            else:
                vname = macrounit['Name']
        if 'Width' in macrounit:
            vwidth = macrounit['Width']
        if 'Height' in macrounit:
            vheight = macrounit['Height']
        formtxt += "\n\n%s%s = xfl.fl_bgn_form(xfl.FL_NO_BOX, %s, %s)\n" % \
                (TWOTABS, prependself(vname), vwidth, vheight)
        self.createformstext.append(formtxt)
        if self.isfirstform:
            self.firstformname = vname
            self.isfirstform = False

    def manage_flendform(self):
        # end FORM area
        formtxt = "\n\n%sxfl.fl_end_form()" % (TWOTABS)
        self.createformstext.append(formtxt)

    def manage_genericflobject(self, macrounit, namepassed):
        # to be used for elements of any flobject
        anyflobjtxt = ""
        if "colors" in macrounit:
            vcolr1, vcolr2 = macrounit['colors'].split()
            anyflobjtxt += "\n%sxfl.fl_set_object_color(%s, %s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vcolr1), \
                    prependxfl(vcolr2))
        if "alignment" in macrounit:            # label alignment
            valignment = macrounit['alignment']
            anyflobjtxt += "\n%sxfl.fl_set_object_lalign(%s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(valignment))
        if "style" in macrounit:
            vstyle = macrounit['style']
            anyflobjtxt += "\n%sxfl.fl_set_object_lstyle(%s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vstyle))
        if "size" in macrounit:
            vsize = macrounit['size']
            anyflobjtxt += "\n%sxfl.fl_set_object_lsize(%s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vsize))
        if "lcol" in macrounit:
            vlcolr = macrounit['lcol']
            anyflobjtxt += "\n%sxfl.fl_set_object_lcol(%s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vlcolr))
        if "resize" in macrounit:
            vresize = macrounit['resize']
            anyflobjtxt += "\n%sxfl.fl_set_object_resize(%s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vresize))
        if "gravity" in macrounit:
            vgrav1, vgrav2 = macrounit['gravity'].split()
            anyflobjtxt += "\n%sxfl.fl_set_object_gravity(%s, %s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vgrav1), \
                    prependxfl(vgrav2))
        if "shortcut" in macrounit:
            if macrounit['shortcut'] is None:   # shortcut unknown
                pass
            else:
                vshcut = macrounit['shortcut']
                anyflobjtxt += "\n%sxfl.fl_set_object_shortcut(%s, \"%s\"," \
                        " 1)" % (TWOTABS, prependself(namepassed), vshcut)
        if "argument" in macrounit:     # strictly relies on cb
            if macrounit['argument'] is None:
                vargum = 0
            else:
                vargum = macrounit['argument']
        if "callback" in macrounit:
            if macrounit['callback'] is None:
                vcallback = ""
            else:
                vcallback = macrounit['callback']
                anyflobjtxt += "\n%sxfl.fl_set_object_callback(%s, %s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependself(vcallback), \
                    vargum)
                cbdef = "\n\n%sdef %s(self, pobj, data):\n%spass" % \
                        (ONETAB, vcallback, TWOTABS)
                self.callbacktext.append(cbdef)
        if "return" in macrounit:
            vreturn = macrounit['return']
            anyflobjtxt += "\n%sxfl.fl_set_object_return(%s, %s)" % \
                    (TWOTABS, prependself(namepassed), prependxfl(vreturn))
        self.createformstext.append(anyflobjtxt)

    def manage_flbegingroup(self, macrounit):
        grouptxt = vname = ""
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flgroupname()
            else:
                vname = macrounit['name']
            grouptxt += "\n%s%s = xfl.fl_bgn_group()" % (TWOTABS, \
                    prependself(vname))
        if "type" in macrounit:
            pass                    # ????
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
            grouptxt += "\n%sxfl.fl_set_object_geometry(%s, %s, %s, %s, " \
                "%s)" % (TWOTABS, prependself(vname), vxpos, vypos, \
                vwidth, vheight)
        if "boxtype" in macrounit:
            vbtype = macrounit['boxtype']
            grouptxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vbtype))
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
            grouptxt += "\n%sxfl.fl_set_object_label(%s, \"%s\")" % \
                    (TWOTABS, prependself(vname), sanitize(vlabel))
        self.createformstext.append(grouptxt)
        return vname

    def manage_flendgroup(self):
        grouptxt = "\n%sxfl.fl_end_group()" % TWOTABS
        self.createformstext.append(grouptxt)

    def manage_flbox(self, macrounit):
        flobjtxt = ""
        if "boxtype" in macrounit:
            vbtype = macrounit['boxtype']
        if "type" in macrounit:
            pass                    # the same as boxtype
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_box(%s, %s, %s, %s, %s, " \
                "\"%s\")" % (TWOTABS, prependself(vname), prependxfl(vbtype), \
                vxpos, vypos, vwidth, vheight, sanitize(vlabel))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flframe(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:     # FL_BORDER_FRAME etc..
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_frame(%s, %s, %s, %s, %s, " \
                "\"%s\")" % (TWOTABS, prependself(vname), prependxfl(vtype), \
                vxpos, vypos, vwidth, vheight, sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fllabelframe(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:     # FL_BORDER_FRAME etc..
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_labelframe(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fltext(self, macrounit):
        vlabel = ""
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_text(%s, %s, %s, %s, %s, " \
                    "\"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, \
                    vheight, sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flbitmap(self, macrounit):
        flobjtxt = ""
        ifuseddata = False
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_bitmap(%s, %s, %s, %s, %s, " \
                "\"%s\")" % \
                (TWOTABS, prependself(vname), prependxfl(vtype), \
                vxpos, vypos, vwidth, vheight, sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if 'width' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            nwidth = macrounit['width']
        if 'height' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            nheight = macrounit['height']
        if 'data' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            ndata = macrounit['data']
        if "fullpath" in macrounit:
            vfullpath = macrounit['fullpath']
        if "file" in macrounit:
            if vfullpath == '1':           # is a full path
                vfile = macrounit['file']
            else:                   # '0', is a relative path
                vfile = './'+macrounit['file']
            if not ifuseddata:      # use file directly
                flobjtxt += "\n%sxfl.fl_set_bitmap_file(%s, \"%s\")" % \
                        (TWOTABS, prependself(vname), vfile)
            else:                   # read data in memory
                # managing import from .xbm data
                vwidth, vheight, vdata = \
                        xfstruct.import_xbmdata_from_file(vfile)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, nwidth, vwidth)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, nheight, vheight)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, ndata, vdata)
                flobjtxt += "\n%sxfl.fl_set_bitmap_data(%s, %s, %s, %s)" \
                        % (TWOTABS, prependself(vname), nwidth, nheight, ndata)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flpixmap(self, macrounit):
        flobjtxt = ""
        ifuseddata = False
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_pixmap(%s, %s, %s, %s, %s, " \
                "\"%s\")" % \
                (TWOTABS, prependself(vname), prependxfl(vtype), \
                vxpos, vypos, vwidth, vheight, sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if 'align' in macrounit:        # pixmap alignment
            valign = macrounit['align']
            flobjtxt += "\n%sxfl.fl_set_pixmap_align(%s, %s, 3, 3)" % \
                    (TWOTABS, prependself(vname), prependxfl(valign))
        if 'data' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            ndata = macrounit['data']
        if "fullpath" in macrounit:
            vfullpath = macrounit['fullpath']
        if "file" in macrounit:
            if vfullpath == '1':           # is a full path
                vfile = macrounit['file']
            else:                   # '0', is a relative path
                vfile = './'+macrounit['file']
            if not ifuseddata:      # use file directly
                flobjtxt += "\n%sxfl.fl_set_pixmap_file(%s, \"%s\")" % \
                        (TWOTABS, prependself(vname), vfile)
            else:                   # read data in memory
                # managing import from .xpm data
                vdata = xfstruct.import_xpmdata_from_file(vfile)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, ndata, vdata)
                flobjtxt += "\n%sxfl.fl_set_pixmap_data(%s, %s)" % \
                    (TWOTABS, prependself(vname), ndata)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flchart(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_chart(%s, %s, %s, %s, %s, " \
                "\"%s\")" % \
                (TWOTABS, prependself(vname), prependxfl(vtype), \
                vxpos, vypos, vwidth, vheight, sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flclock(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_clock(%s, %s, %s, %s, %s, " \
                    "\"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_button(%s, %s, %s, %s, %s, " \
                    "\"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flroundbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_roundbutton(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        if "value" in macrounit:
            vvalue = macrounit['value']
            if vvalue == '1':       # if it is to be set
                flobjtxt += "\n%sxfl.fl_set_button(%s, 1)" % \
                    (TWOTABS, prependself(vname))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flround3dbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_round3dbutton(%s, %s, %s, %s, " \
                "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        if "value" in macrounit:
            vvalue = macrounit['value']
            if vvalue == '1':       # if it is to be set
                flobjtxt += "\n%sxfl.fl_set_button(%s, 1)" % \
                    (TWOTABS, prependself(vname))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flcheckbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_checkbutton(%s, %s, %s, %s, " \
                "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        if "value" in macrounit:
            vvalue = macrounit['value']
            if vvalue == '1':       # if it is to be set
                flobjtxt += "\n%sxfl.fl_set_button(%s, 1)" % \
                    (TWOTABS, prependself(vname))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fllightbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_lightbutton(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        if "value" in macrounit:
            vvalue = macrounit['value']
            if vvalue == '1':       # if it is to be set
                flobjtxt += "\n%sxfl.fl_set_button(%s, 1)" % \
                    (TWOTABS, prependself(vname))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flscrollbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_scrollbutton(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flbitmapbutton(self, macrounit):
        flobjtxt = ""
        ifuseddata = False
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_bitmapbutton(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        if 'width' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            nwidth = macrounit['width']
        if 'height' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            nheight = macrounit['height']
        if 'data' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            ndata = macrounit['data']
        if "fullpath" in macrounit:
            vfullpath = macrounit['fullpath']
        if "file" in macrounit:
            if vfullpath == '1':           # is a full path
                vfile = macrounit['file']
            else:                          # is a relative path
                vfile = './'+macrounit['file']
            if not ifuseddata:          # use file directly
                flobjtxt += "\n%sxfl.fl_set_bitmapbutton_file(%s, \"%s\")" % \
                        (TWOTABS, prependself(vname), vfile)
            else:                   # read data in memory
                # managing import from .xbm data
                vwidth, vheight, vdata = \
                        xfstruct.import_xbmdata_from_file(vfile)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, nwidth, vwidth)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, nheight, vheight)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, ndata, vdata)
                flobjtxt += "\n%sxfl.fl_set_bitmapbutton_data(%s, %s, %s, %s)" \
                        % (TWOTABS, prependself(vname), nwidth, nheight, ndata)
        # 'helper' not implemented upstreams
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flpixmapbutton(self, macrounit):
        flobjtxt = ""
        vfocus = "1"    # focus on by default
        ifuseddata = False
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_pixmapbutton(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        if 'align' in macrounit:        # pixmap alignment
            valign = macrounit['align']
            flobjtxt += "\n%sxfl.fl_set_pixmapbutton_align(%s, %s, 3, 3)" % \
                    (TWOTABS, prependself(vname), prependxfl(valign))
        if 'helper' in macrounit:
            vhelper = macrounit['helper']
            flobjtxt += "\n%sxfl.fl_set_object_helper(%s, \"%s\")" % \
                    (TWOTABS, prependself(vname), \
                    sanitize(prependxfl(vhelper)))
        if 'data' in macrounit:         # if "Use data" enabled
            ifuseddata = True
            ndata = macrounit['data']
        if "fullpath" in macrounit:
            vfullpath = macrounit['fullpath']
        if "file" in macrounit:
            if vfullpath == '1':           # is a full path
                vfile = macrounit['file']
            else:                   # '0', is a relative path
                vfile = './'+macrounit['file']
            if not ifuseddata:          # use file directly
                flobjtxt += "\n%sxfl.fl_set_pixmapbutton_file(%s, \"%s\")" % \
                        (TWOTABS, prependself(vname), vfile)
            else:                   # read data in memory
                # managing import from .xpm data
                vdata = xfstruct.import_xpmdata_from_file(vfile)
                flobjtxt += "\n%s%s = %s" % (TWOTABS, ndata, vdata)
                flobjtxt += "\n%sxfl.fl_set_pixmapbutton_data(%s, %s)" % \
                    (TWOTABS, prependself(vname), ndata)
        if "focus" in macrounit:
            vfocus = macrounit['focus']
        if "focus_file" in macrounit:
            if vfocus == "1":     # focus file in use
                if vfullpath == '1':           # is a full path
                    vfocusfile = macrounit['focus_file']
                else:                   # '0', is a relative path
                    vfocusfile = './'+macrounit['focus_file']
                flobjtxt += "\n%sxfl.fl_set_pixmapbutton_focus_file(%s, " \
                        "\"%s\")" % (TWOTABS, prependself(vname), vfocusfile)
            else:                # no focus file used
                pass
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fllabelbutton(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_labelbutton(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "mbuttons" in macrounit:
            vmbuttons = macrounit['mbuttons']
            flobjtxt += "\n%sxfl.fl_set_button_mouse_buttons(%s, %s)" % \
                    (TWOTABS, prependself(vname), vmbuttons)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flslider(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_slider(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_slider_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_slider_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "increment" in macrounit:
            vleftincr, vrightincr = macrounit['increment'].split()
            flobjtxt += "\n%sxfl.fl_set_slider_increment(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vleftincr, vrightincr)
        if "slsize" in macrounit:
            vslsize = macrounit['slsize']
            flobjtxt += "\n%sxfl.fl_set_slider_size(%s, %s)" % \
                    (TWOTABS, prependself(vname), vslsize)
        if "step" in macrounit:
            vstep = macrounit['step']
            flobjtxt += "\n%sxfl.fl_set_slider_step(%s, %s)" % \
                    (TWOTABS, prependself(vname), vstep)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flvalslider(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_valslider(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_slider_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_slider_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "increment" in macrounit:
            vleftincr, vrightincr = macrounit['increment'].split()
            flobjtxt += "\n%sxfl.fl_set_slider_increment(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vleftincr, vrightincr)
        if "slsize" in macrounit:
            vslsize = macrounit['slsize']
            flobjtxt += "\n%sxfl.fl_set_slider_size(%s, %s)" % \
                    (TWOTABS, prependself(vname), vslsize)
        if "step" in macrounit:
            vstep = macrounit['step']
            flobjtxt += "\n%sxfl.fl_set_slider_step(%s, %s)" % \
                    (TWOTABS, prependself(vname), vstep)
        if "precision" in macrounit:
            vprecis = macrounit['precision']
            flobjtxt += "\n%sxfl.fl_set_slider_precision(%s, %s)" % \
                    (TWOTABS, prependself(vname), vprecis)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flscrollbar(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_scrollbar(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_scrollbar_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_scrollbar_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "increment" in macrounit:
            vleftincr, vrightincr = macrounit['increment'].split()
            flobjtxt += "\n%sxfl.fl_set_scrollbar_increment(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vleftincr, vrightincr)
        if "slsize" in macrounit:
            vslsize = macrounit['slsize']
            flobjtxt += "\n%sxfl.fl_set_scrollbar_size(%s, %s)" % \
                    (TWOTABS, prependself(vname), vslsize)
        if "step" in macrounit:
            vstep = macrounit['step']
            flobjtxt += "\n%sxfl.fl_set_scrollbar_step(%s, %s)" % \
                    (TWOTABS, prependself(vname), vstep)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fldial(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_dial(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_dial_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_dial_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "step" in macrounit:
            vstep = macrounit['step']
            flobjtxt += "\n%sxfl.fl_set_dial_step(%s, %s)" % \
                    (TWOTABS, prependself(vname), vstep)
        if "angles" in macrounit:
            vminangl, vmaxangl = macrounit['angles'].split()
            flobjtxt += "\n%sxfl.fl_set_dial_angles(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminangl, vmaxangl)
        if "dir" in macrounit:
            vdir = macrounit['dir']
            flobjtxt += "\n%sxfl.fl_set_dial_direction(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vdir))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flpositioner(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_positioner(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "xbounds" in macrounit:
            vxminbnd, vxmaxbnd = macrounit['xbounds'].split()
            flobjtxt += "\n%sxfl.fl_set_positioner_xbounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vxminbnd, vxmaxbnd)
        if "ybounds" in macrounit:
            vyminbnd, vymaxbnd = macrounit['ybounds'].split()
            flobjtxt += "\n%sxfl.fl_set_positioner_ybounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vyminbnd, vymaxbnd)
        if "xvalue" in macrounit:
            vxvalue = macrounit['xvalue']
            flobjtxt += "\n%sxfl.fl_set_positioner_xvalue(%s, %s)" % \
                    (TWOTABS, prependself(vname), vxvalue)
        if "yvalue" in macrounit:
            vyvalue = macrounit['yvalue']
            flobjtxt += "\n%sxfl.fl_set_positioner_yvalue(%s, %s)" % \
                    (TWOTABS, prependself(vname), vyvalue)
        if "xstep" in macrounit:
            vxstep = macrounit['xstep']
            flobjtxt += "\n%sxfl.fl_set_positioner_xstep(%s, %s)" % \
                    (TWOTABS, prependself(vname), vxstep)
        if "ystep" in macrounit:
            vystep = macrounit['ystep']
            flobjtxt += "\n%sxfl.fl_set_positioner_ystep(%s, %s)" % \
                    (TWOTABS, prependself(vname), vystep)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flthumbwheel(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_thumbwheel(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_thumbwheel_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_thumbwheel_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "step" in macrounit:
            vstep = macrounit['step']
            flobjtxt += "\n%sxfl.fl_set_thumbwheel_step(%s, %s)" % \
                    (TWOTABS, prependself(vname), vstep)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flcounter(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_counter(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_counter_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_counter_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "step" in macrounit:
            vsmstep, vlgstep = macrounit['step'].split()
            flobjtxt += "\n%sxfl.fl_set_counter_step(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vsmstep, vlgstep)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flspinner(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_spinner(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "bounds" in macrounit:
            vminbnd, vmaxbnd = macrounit['bounds'].split()
            flobjtxt += "\n%sxfl.fl_set_spinner_bounds(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vminbnd, vmaxbnd)
        if "value" in macrounit:
            vvalue = macrounit['value']
            flobjtxt += "\n%sxfl.fl_set_spinner_value(%s, %s)" % \
                    (TWOTABS, prependself(vname), vvalue)
        if "precision" in macrounit:
            vprecis = macrounit['precision']
            flobjtxt += "\n%sxfl.fl_set_spinner_precision(%s, %s)" % \
                    (TWOTABS, prependself(vname), vprecis)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flinput(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_input(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flbrowser(self, macrounit):
        # TODO: only one line to be added (last one) is supported here
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_browser(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "h_pref" in macrounit:
            vhpref = macrounit['h_pref']
            flobjtxt += "\n%sxfl.fl_set_browser_hscrollbar(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vhpref))
        if "v_pref" in macrounit:
            vvpref = macrounit['v_pref']
            flobjtxt += "\n%sxfl.fl_set_browser_vscrollbar(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vvpref))
        if "contents" in macrounit:
            vcontents = macrounit['contents']
            flobjtxt += "\n%sxfl.fl_add_browser_line(%s, \"%s\")" % \
                    (TWOTABS, prependself(vname), vcontents)
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fltimer(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_timer(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flxyplot(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_xyplot(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        if "xtics" in macrounit:
            vmaxxtics, vminxtics = macrounit['xtics'].split()
            flobjtxt += "\n%sxfl.fl_set_xyplot_xtics(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vmaxxtics, vminxtics)
        if "ytics" in macrounit:
            vmaxytics, vminytics = macrounit['ytics'].split()
            flobjtxt += "\n%sxfl.fl_set_xyplot_ytics(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), vmaxytics, vminytics)
        if "xscale" in macrounit:
            vxscale, vxbase = macrounit['xscale'].split()
            flobjtxt += "\n%sxfl.fl_set_xyplot_xscale(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vxscale), vxbase)
        if "yscale" in macrounit:
            vyscale, vybase = macrounit['yscale'].split()
            flobjtxt += "\n%sxfl.fl_set_xyplot_yscale(%s, %s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vyscale), vybase)
        if "grid" in macrounit:
            vxgrid, vygrid = macrounit['grid'].split()
            flobjtxt += "\n%sxfl.fl_set_xyplot_xgrid(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vxgrid))
            flobjtxt += "\n%sxfl.fl_set_xyplot_ygrid(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vygrid))
        if "gridstyle" in macrounit:
            vgridstyle = macrounit['gridstyle']
            flobjtxt += "\n%sxfl.fl_set_xyplot_grid_linestyle(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vgridstyle))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flcanvas(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_canvas(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flglcanvas(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_glcanvas(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_fltabfolder(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_tabfolder(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flformbrowser(self, macrounit):
        flobjtxt = ""
        if "type" in macrounit:
            vtype = prependfltype(macrounit['type'])
        if "box" in macrounit:
            vxpos, vypos, vwidth, vheight = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                vlabel = ""
            else:
                vlabel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                vname = self.getgeneric_flobjname()
            else:
                vname = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_formbrowser(%s, %s, %s, %s, " \
                    "%s, \"%s\")" % (TWOTABS, prependself(vname), \
                    prependxfl(vtype), vxpos, vypos, vwidth, vheight, \
                    sanitize(vlabel))
        if "boxtype" in macrounit:
            vboxtype = macrounit['boxtype']
            flobjtxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(vname), prependxfl(vboxtype))
        self.createformstext.append(flobjtxt)
        return vname

    def manage_flfree(self, macrounit):
        pass

    def manage_flnmenu(self, macrounit):   # not implemented upstreams yet
        pass

    def manage_flselect(self, macrounit):   # not implemented upstreams yet
        pass

    def manage_endmain(self):
        # append text at the end of main func
        endingstxt = "\n%sself.create_forms()" % TWOTABS
        endingstxt += "\n%sxfl.fl_show_form(%s, xfl.FL_PLACE_CENTERFREE, " \
                "xfl.FL_FULLBORDER, \"%s\")" % (TWOTABS, \
                prependself(self.firstformname), self.firstformname)
        endingstxt += "\n\n%swhile xfl.fl_do_forms():\n%s%spass" % \
                (TWOTABS, TWOTABS, ONETAB)
        endingstxt += "\n\n%sxfl.fl_finish()" % TWOTABS
        self.endmaintext.append(endingstxt)

    def manage_endings(self):
        # append text of code run to func list
        filname = self.infile.replace(".fd", ".py")
        endingstxt = "\n\n\nif __name__ == '__main__':"
        endingstxt += '\n%sprint "***** %s *****"' % (ONETAB, filname)
        endingstxt += "\n%sApplDemo = %s(len(sys.argv), sys.argv)\n\n" % \
                (ONETAB, self.appname)
        self.runcodetext.append(endingstxt)

    def savepyfile(self):
        # save elements of func lists in .py file
        try:
            fdout = open(self.outfile, 'w')
        except IOError:
            message = "Cannot write %s on disk" % self.outfile
            errorcliargs(message, 5)
        else:
            try:
                for line in self.headertext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.inittext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.maintext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.endmaintext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.preformtext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.createformstext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.callbacktext:
                    if not line:
                        break
                    fdout.write(line)
                for line in self.runcodetext:
                    if not line:
                        break
                    fdout.write(line)
                fdout.close()
            except IOError:
                message = "Cannot write %s on disk" % self.outfile
                errorcliargs(message, 5)
            else:
                message = "%s successfully created." % self.outfile
                print(message)

if __name__ == '__main__':
    FdConvertToPy(len(sys.argv), sys.argv)

