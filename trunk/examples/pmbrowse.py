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
import xformslib as xfl


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
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.fd_ttt = self.create_form_ttt()
        xfl.fl_show_form(self.fd_ttt.ttt, xfl.FL_PLACE_CENTER, \
                xfl.FL_TRANSIENT, "PixmapBrowser")
        xfl.fl_set_fselector_placement(xfl.FL_PLACE_FREE)
        xfl.fl_set_fselector_callback(self.load_file, 0)
        xfl.fl_show_fselector("Load a Pixmap file", "", "*.x?m", "")
        xfl.fl_do_forms()


    def create_form_ttt(self):
        fdui = FD_ttt()
        fdui.ttt = xfl.fl_bgn_form(xfl.FL_NO_BOX, 330, 320)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 330, 320, "")
        fdui.bm = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 30, 20, 270, \
                240, "")
        xfl.fl_set_object_boxtype(fdui.bm, xfl.FL_FLAT_BOX)
        fdui.pm = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 30, 20, 270, \
                240, "")
        xfl.fl_set_object_boxtype(fdui.pm, xfl.FL_FLAT_BOX)
        fdui.done = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 220, 280, \
                90, 30, "Done")
        xfl.fl_set_object_lalign(fdui.done, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.done,self. done, 0)
        fdui.load = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 280, \
                90, 30, "Load")
        xfl.fl_set_button_shortcut(fdui.load, "L", 1)
        xfl.fl_set_object_lalign(fdui.load, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.load, self.reloadfile, 0)
        xfl.fl_end_form()
        return fdui


    def load_file(self, fname, pvdata):
        #ldata = xfl.fls_convert_ptrvoid_to_ptrlongc(pvdata).contents.value
        #print("ldata", ldata)
        if not fname or not os.path.exists(fname):
            print("Missing file name\n")
            return 0
        fnameonly = os.path.basename(fname)
        if os.path.isdir(fname):
            xfl.fl_set_directory(fname)
        else:   # a file
            p, ext = os.path.splitext(fnameonly)
            if not ext:
                print("Missing file extension\n")
                return 0
            else:
                if fname.endswith(".xpm"):
                    xfl.fl_hide_object(self.fd_ttt.bm)
                    xfl.fl_free_pixmap_pixmap(self.fd_ttt.pm)
                    xfl.fl_set_pixmap_file(self.fd_ttt.pm, fname)
                    xfl.fl_show_object(self.fd_ttt.pm)
                elif fname.endswith(".xbm"):
                    xfl.fl_hide_object(self.fd_ttt.pm)
                    xfl.fl_set_bitmap_file(self.fd_ttt.bm, fname)
                    xfl.fl_show_object(self.fd_ttt.bm)
                else:
                    message = "Invalid file extension, neither" \
                            ".xpm nor .xbm file: %s\n" % ext
                    print message
                    return 0
        return 1


    def done(self, pobj, q):
        xfl.fl_finish()
        sys.exit(0)


    def reloadfile(self, pobj, q):
        xfl.fl_set_fselector_placement(xfl.FL_PLACE_MOUSE)
        xfl.fl_set_fselector_callback(self.load_file, 0)
        xfl.fl_show_fselector("Load a Pix/bitMap file", "", "", "")


if __name__ == '__main__':
    print ("********* pmbrowse.py *********")
    Flpmbrowse(len(sys.argv), sys.argv)
