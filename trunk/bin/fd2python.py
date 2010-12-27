#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's script to convert fdesign '.fd' files to python UI layout.
"""

#    Copyright (C) 2010  Luca Lazzaroni "LukenShiro"
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
from xformslib import vers

# constants
ONETAB = "    "
TWOTABS = ONETAB * 2


def xfcopyright():
    print('xforms-python conversion script from fdesign .fd files to' \
            ' python UI layout\nIt is part of xforms-python version ' \
            '%s\nCopyright (C) 2010  Luca Lazzaroni "LukenShiro"\n' \
            'It is released under LGPL 2.1 license. See LICENSE file' \
            ' for details.\n' % vers.__version__)

def errorcliargs(msg="", exval=0):
    if exval > 0:
        print("Fatal error: %s\n" % msg)
    print("Usage: fd2python <infile>.fd [<outfile>.py]\n" \
            "If <outfile>.py is omitted, <infile>.py is used\n" \
            "<outfile>.py should not be existing.")
    sys.exit(exval)

def prependxflvalue(valuestr):
    if valuestr.startswith("FL_"):
        valuestr = "xfl."+valuestr
    return valuestr

def prependself(valuestr):
    if valuestr:
        valuestr = "self."+valuestr
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

        self.infile = ""
        self.outfile = ""

        xfcopyright()
        if self.cliargs(lsysargv, sysargv):
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
        # verify if .fd compliant format
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
        thereisform = 0
        thereisflobj = 0

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
                thereisform = 1
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
                thereisflobj = 1
            elif "==============================" in line:      # EOF
                self.listpairsofelem[elemnum] = "<ENDFLOBJ>", None
                elemnum += 1
                self.listpairsofelem[elemnum] = "<ENDALL>", None
                elemnum += 1
                break
            else:
                linenew = line.strip()
                try:
                    mykey, myvalue = linenew.split(':')
                except ValueError:      # not a key (remove element)
                    continue
                else:
                    if not myvalue:     # not a value (placeholder)
                        myvalue = None
                mykey = mykey.strip()
                if myvalue:
                    myvalue = myvalue.strip()
                self.listpairsofelem[elemnum] = mykey, myvalue
                elemnum += 1
        fdin.close()
        #print self.listpairsofelem

    def convertlistsindict(self):
        #return 0
        # organize key-value pairs in dict
        self.listdictsofelem = []   #* (len(self.listpairsofelem)/2)

        #print self.listdictsofelem
        unitold = 0     # a key-value pair of old list
        unitnew = 0     # a block belonging to intro or form header or flobj
        while True:
            elem = self.listpairsofelem[unitold]
            if elem[0] == "<INTRO>":
                singdict = {'phase' : 'INTRO'}
                unitold += 1
            elif elem[0] == "<ENDINTRO>":
                self.listdictsofelem.append(singdict)
                del singdict
                unitold += 1
                unitnew += 1
            elif elem[0] == "<FORM>":
                singdict = {'phase' : 'FORM'}
                unitold += 1
            elif elem[0] == "<ENDFORMHEAD>":
                self.listdictsofelem.append(singdict)
                del singdict
                unitold += 1
                unitnew += 1
            elif elem[0] == "<FLOBJ>":
                singdict = {'phase' : 'FLOBJ'}
                unitold += 1
            elif elem[0] == "<ENDFLOBJ>":
                self.listdictsofelem.append(singdict)
                del singdict
                unitold += 1
                unitnew += 1
            elif elem[0] == "<ENDALL>":
                singdict = {'phase' : 'ENDFORM'}
                self.listdictsofelem.append(singdict)
                break
            elif elem[0] == "<ENDFORM>":
                singdict = {'phase' : 'ENDFORM'}
                self.listdictsofelem.append(singdict)
                del singdict
                unitold += 1            # next
                unitnew += 1
            else:               # real key-value pair
                if singdict:
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
                    self.manage_flbegingroup(macrounit)
                elif macrounit['class'] == 'FL_END_GROUP':
                    self.manage_flendgroup()
                elif macrounit['class'] == 'FL_BITMAP':
                    pass
                elif macrounit['class'] == 'FL_BOX':
                    self.manage_flbox(macrounit)
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
            self.gropnum += 1
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
        appname = self.infile.replace(".fd", "").replace("-", "_").capitalize()
        introtxt = "\nimport sys\nimport xformslib as xfl\n\nclass %s" \
                "(object):\n%sdef __init__(self, lsysargv, sysargv):" \
                "\n%sxfl.fl_initialize(lsysargv, sysargv, '%s', None, 0)\n" % \
                (appname, ONETAB, TWOTABS, appname)
        self.inittext.append(introtxt)

    def manage_intro(self, macrounit):
        # INTRO area
        introtxt = ""
        if "Number of forms" in macrounit:
            self.numforms = macrounit["Number of forms"]
        if "Unit of measure" in macrounit:
            value = macrounit['Unit of measure']
            introtxt = "\n%sxfl.fl_set_coordunit(%s)" % \
                    (TWOTABS, prependxflvalue(value))
        if "Border Width" in macrounit:
            value = macrounit['Border Width']
            introtxt = "\n%sxfl.fl_set_border_width(%s)" % (TWOTABS, value)
        self.inittext.append(introtxt)

    def manage_preform(self):
        preform = "\n\n%sdef createforms(self):" % ONETAB
        self.preformtext.append(preform)

    def manage_flbeginform(self, macrounit):
        # FORM area
        formtxt = ""
        if "Number of Objects" in macrounit:    # unused here currently
            self.numflobjs = macrounit['Number of Objects']
        if "Name" in macrounit:
            if macrounit['Name'] is None:       # name unknown
                name = self.getgeneric_flformname()
            else:
                name = macrounit['Name']
        if 'Width' in macrounit:
            valuew = macrounit['Width']
        if 'Height' in macrounit:
            valueh = macrounit['Height']
        formtxt += "\n\n%s%s = xfl.fl_bgn_form(xfl.FL_NO_BOX, %s, %s)" % \
                (TWOTABS, prependself(name), valuew, valueh)
        self.createformstext.append(formtxt)

    def manage_flendform(self):
        # end FORM area
        formtxt = "\n%sxfl.fl_end_form()" % (TWOTABS)
        self.createformstext.append(formtxt)

    def manage_flbegingroup(self, macrounit):
        grouptxt = ""
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                name = self.getgeneric_flgroupname()
            else:
                name = macrounit['name']
            grouptxt += "\n%s%s = xfl.fl_bgn_group()" % (TWOTABS, \
                    prependself(name))
        if "type" in macrounit:
            pass                    # ????
        if "box" in macrounit:
            valuex, valuey, valuew, valueh = macrounit['box'].split()
            grouptxt += "\n%sxfl.fl_set_geometry(%s, %s, %s, %s, %s)" % \
                    (TWOTABS, prependself(name), valuex, valuey, \
                    valuew, valueh)
        if "boxtype" in macrounit:
            valuebt = macrounit['boxtype']
            grouptxt += "\n%sxfl.fl_set_object_boxtype(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuebt))
        if "colors" in macrounit:
            valuec1, valuec2 = macrounit['colors'].split()
            grouptxt += "\n%sxfl.fl_set_object_color(%s, %s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuec1), \
                    prependxflvalue(valuec2))
        if "alignment" in macrounit:
            valuea = macrounit['alignment']
            grouptxt += "\n%sxfl.fl_set_object_lalign(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuea))
        if "style" in macrounit:
            values = macrounit['style']
            grouptxt += "\n%sxfl.fl_set_object_lstyle(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(values))
        if "size" in macrounit:
            values = macrounit['size']
            grouptxt += "\n%sxfl.fl_set_object_lsize(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(values))
        if "lcol" in macrounit:
            valuelc = macrounit['lcol']
            grouptxt += "\n%sxfl.fl_set_object_lcol(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuelc))
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                valuel = ""
            else:
                valuel = macrounit['label']
            grouptxt += "\n%sxfl.fl_set_object_label(%s, \'%s\')" % \
                    (TWOTABS, prependself(name), valuel)
        if "shortcut" in macrounit:
            if macrounit['shortcut'] is None:   # shortcut unknown
                pass
            else:
                values = macrounit['shortcut']
                grouptxt += "\n%sxfl.fl_set_object_shortcut(%s, %s)" % \
                    (TWOTABS, prependself(name), values)
        if "resize" in macrounit:
            valuer = macrounit['resize']
            grouptxt += "\n%sxfl.fl_set_object_resize(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuer))
        if "gravity" in macrounit:
            valueg1, valueg2 = macrounit['gravity'].split()
            grouptxt += "\n%sxfl.fl_set_object_gravity(%s, %s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valueg1), \
                    prependxflvalue(valueg2))
        if "argument" in macrounit:     # strictly relies on cb
            if macrounit['argument'] is None:
                argum = 0
            else:
                argum = macrounit['argument']
        if "callback" in macrounit:
            if macrounit['callback'] is None:
                callback = ""
            else:
                callback = macrounit['callback']
                grouptxt += "\n%sxfl.fl_set_object_callback(%s, %s, %s)" % \
                    (TWOTABS, prependself(name), prependself(callback), argum)
                cbdef = "\n%sdef %s(self, r):\n%spass" % \
                        (ONETAB, callback, TWOTABS)
                self.callbacktext.append(cbdef)
        if "return" in macrounit:
            valuer = macrounit['return']
            grouptxt += "\n%sxfl.fl_set_object_return(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuer))
        self.createformstext.append(grouptxt)

    def manage_flendgroup(self):
        grouptxt = "\n%sxfl.fl_end_group()" % TWOTABS
        self.createformstext.append(grouptxt)

    def manage_flbitmap(self):
        pass

    def manage_flbitmapbutton(self):
        pass

    def manage_flbox(self, macrounit):
        flobjtxt = ""
        if "boxtype" in macrounit:     # connected to name, box
            valuetype = macrounit['boxtype']
        if "box" in macrounit:
            valuex, valuey, valuew, valueh = macrounit['box'].split()
        if "label" in macrounit:
            if macrounit['label'] is None:      # label unknown
                valuel = ""
            else:
                valuel = macrounit['label']
        if "name" in macrounit:
            if macrounit['name'] is None:       # name unknown
                name = self.getgeneric_flobjname()
            else:
                name = macrounit['name']
            flobjtxt += "\n%s%s = xfl.fl_add_box(%s, %s, %s, %s, %s, " \
                "\'%s\')" % \
                (TWOTABS, prependself(name), prependxflvalue(valuetype), \
                valuex, valuey, valuew, valueh, valuel)
        if "colors" in macrounit:
            valuec1, valuec2 = macrounit['colors'].split()
            flobjtxt += "\n%sxfl.fl_set_object_color(%s, %s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuec1), \
                    prependxflvalue(valuec2))
        if "alignment" in macrounit:
            valuea = macrounit['alignment']
            flobjtxt += "\n%sxfl.fl_set_object_lalign(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuea))
        if "style" in macrounit:
            values = macrounit['style']
            flobjtxt += "\n%sxfl.fl_set_object_lstyle(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(values))
        if "size" in macrounit:
            values = macrounit['size']
            flobjtxt += "\n%sxfl.fl_set_object_lsize(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(values))
        if "lcol" in macrounit:
            valuelc = macrounit['lcol']
            flobjtxt += "\n%sxfl.fl_set_object_lcol(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuelc))
        if "shortcut" in macrounit:
            if macrounit['shortcut'] is None:   # shortcut unknown
                pass
            else:
                values = macrounit['shortcut']
                flobjtxt += "\n%sxfl.fl_set_object_shortcut(%s, %s)" % \
                    (TWOTABS, prependself(name), values)
        if "resize" in macrounit:
            valuer = macrounit['resize']
            flobjtxt += "\n%sxfl.fl_set_object_resize(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuer))
        if "gravity" in macrounit:
            valueg1, valueg2 = macrounit['gravity'].split()
            flobjtxt += "\n%sxfl.fl_set_object_gravity(%s, %s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valueg1), \
                    prependxflvalue(valueg2))
        if "argument" in macrounit:     # strictly relies on cb
            if macrounit['argument'] is None:
                argum = 0
            else:
                argum = macrounit['argument']
        if "callback" in macrounit:
            if macrounit['callback'] is None:
                callback = ""
            else:
                callback = macrounit['callback']
                flobjtxt += "\n%sxfl.fl_set_object_callback(%s, %s, %s)" % \
                    (TWOTABS, prependself(name), prependself(callback), argum)
                cbdef = "\n\n%sdef %s(self, r):\n%spass" % \
                        (ONETAB, callback, TWOTABS)
                self.callbacktext.append(cbdef)
        if "return" in macrounit:
            if macrounit['return'] is None:
                pass
            else:
                valuer = macrounit['return']
                flobjtxt += "\n%sxfl.fl_set_object_return(%s, %s)" % \
                    (TWOTABS, prependself(name), prependxflvalue(valuer))
        self.createformstext.append(flobjtxt)


    def manage_flbrowser(self):
        pass

    def manage_flbutton(self):
        pass

    def manage_flcanvas(self):
        pass

    def manage_flchart(self):
        pass

    def manage_flcheckbutton(self):
        pass

    def manage_flclock(self):
        pass

    def manage_flcounter(self):
        pass

    def manage_fldial(self):
        pass

    def manage_flformbrowser(self):
        pass

    def manage_flframe(self):
        pass

    def manage_flinput(self):
        pass

    def manage_fllabelframe(self):
        pass

    def manage_fllightbutton(self):
        pass

    def manage_flnmenu(self):
        pass

    def manage_flpixmap(self):
        pass

    def manage_flpixmapbutton(self):
        pass

    def manage_flpositioner(self):
        pass

    def manage_flround3dbutton(self):
        pass

    def manage_flselect(self):
        pass

    def manage_flslider(self):
        pass

    def manage_flspinner(self):
        pass

    def manage_fltabfolder(self):
        pass

    def manage_fltext(self):
        pass

    def manage_flthumbwheel(self):
        pass

    def manage_flvalslider(self):
        pass

    def manage_endmain(self):
        # append text at the end of main func
        endingstxt = "\n%sself.createforms()\n\n%sxfl.fl_finish()" % \
                (TWOTABS, TWOTABS)
        self.endmaintext.append(endingstxt)

    def manage_endings(self):
        # append text of code run to func list
        appname = self.infile.replace(".fd", "").replace("-", "_").capitalize()
        endingstxt = "\n\n\nif __name__ == '__main__':\n%sApplrun = " \
                "%s(len(sys.argv), sys.argv)" % (ONETAB, appname)
        self.runcodetext.append(endingstxt)

    def savepyfile(self):
        # save elements of func lists in .py file
        try:
            fdout = open(self.outfile, 'w')
        except IOError:
            errcliargs("Cannot write <outfile>.py on disk.", 5)
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
                errcliargs("Cannot write <outfile>.py on disk", 5)


if __name__ == '__main__':
    FdConvertToPy(len(sys.argv), sys.argv)

