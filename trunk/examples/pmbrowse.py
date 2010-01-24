#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  pmbrowse.c XForms demo, with some adaptations and modifications.
#
#  pmbrowse.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Showing the use of non-modal file selector
#

import sys, os
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbrowser import *
from xformslib.flbutton import *
from xformslib.flbitmap import *
from xformslib.flmisc import *
from xformslib.flgoodies import *
from xformslib.xfdata import *




# Forms and Objects

class FD_ttt(object):
    ttt = None
    vdata = None
    cdata = ""
    ldata = 0
    bm = None
    pm = None
    done = None
    load = None


class Flpmbrowse(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_ttt = self.create_form_ttt()

        fl_show_form(self.fd_ttt.ttt, FL_PLACE_CENTER, FL_TRANSIENT, \
                     "PixmapBrowser")

        fl_set_fselector_placement(FL_PLACE_FREE)
        fl_set_fselector_callback(self.load_file, 0)
        fl_show_fselector("Load a Pixmap file", None, "*.x?m", None)
        fl_do_forms()


    def create_form_ttt(self):

        fdui = FD_ttt()

        fdui.ttt = fl_bgn_form(FL_NO_BOX, 330, 320)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 330, 320, "")

        fdui.bm = fl_add_bitmap(FL_NORMAL_BITMAP, 30, 20, 270, 240, "")
        fl_set_object_boxtype(fdui.bm, FL_FLAT_BOX)

        fdui.pm = fl_add_pixmap(FL_NORMAL_PIXMAP, 30, 20, 270, 240, "")
        fl_set_object_boxtype(fdui.pm, FL_FLAT_BOX)

        fdui.done = fl_add_button(FL_NORMAL_BUTTON, 220, 280, 90, 30, "Done")
        fl_set_object_lalign(fdui.done, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.done,self. done, 0)

        fdui.load = fl_add_button(FL_NORMAL_BUTTON, 20, 280, 90, 30, "Load")
        fl_set_button_shortcut(fdui.load, "L", 1)
        fl_set_object_lalign(fdui.load, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.load, self.reloadfile, 0)

        fl_end_form()
        return fdui


    def load_file(self, fname, data):

        if not fname or not os.path.exists(fname):
            print "Missing file name\n"
            return 0

        fnameonly = os.path.basename(fname)
        if not os.path.isdir(fname):
            p, ext = os.path.splitext(fnameonly)
            if not ext:
                print "Missing file extension\n"
                return 0
            else:
                if fname.endswith(".xpm"):
                    fl_hide_object(self.fd_ttt.bm)
                    fl_free_pixmap_pixmap(self.fd_ttt.pm)
                    fl_set_pixmap_file(self.fd_ttt.pm, fname)
                    fl_show_object(self.fd_ttt.pm)
                elif fname.endswith(".xbm"):
                    fl_hide_object(self.fd_ttt.pm)
                    fl_set_bitmap_file(self.fd_ttt.bm, fname)
                    fl_show_object(self.fd_ttt.bm)
                else:
                    print "Invalid file extension: %s\n" % ext
                    return 0
        return 1


    def done(self, pobj, q):
        fl_finish()
        sys.exit(0)


    def reloadfile(self, pobj, q):
        fl_set_fselector_placement(FL_PLACE_MOUSE)
        fl_set_fselector_callback(self.load_file, 0)
        fl_show_fselector("Load a Pix/bitMap file", None, None, None)




if __name__ == '__main__':
    Flpmbrowse(len(sys.argv), sys.argv)

