#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  pmbrowse.c XForms demo, with some adaptations.
#
#  pmbrowse.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Showing the use of non-modal file selector
#

import sys, os
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc




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


def create_form_ttt():

    fdui = FD_ttt()

    fdui.ttt = xf.fl_bgn_form(xfc.FL_NO_BOX, 330, 320)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 330, 320, "")

    fdui.bm = xf.fl_add_bitmap(xfc.FL_NORMAL_BITMAP, 30, 20, 270, 240, "")
    xf.fl_set_object_boxtype(fdui.bm, xfc.FL_FLAT_BOX)

    fdui.pm = xf.fl_add_pixmap(xfc.FL_NORMAL_PIXMAP, 30, 20, 270, 240, "")
    xf.fl_set_object_boxtype(fdui.pm, xfc.FL_FLAT_BOX)

    fdui.done = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 220, 280, 90, 30, "Done")
    xf.fl_set_object_lalign(fdui.done, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.done, done, 0)

    fdui.load = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 280, 90, 30, "Load")
    xf.fl_set_button_shortcut(fdui.load, "L", 1)
    xf.fl_set_object_lalign(fdui.load, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.load, reloadfile, 0)

    xf.fl_end_form()

    return fdui



def main(lsysargv, sysargv):
    global fd_ttt

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    fd_ttt = create_form_ttt()

    xf.fl_show_form(fd_ttt.ttt, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                    "PixmapBrowser")

    xf.fl_set_fselector_placement(xfc.FL_PLACE_FREE)
    xf.fl_set_fselector_callback(load_file, 0)
    xf.fl_show_fselector("Load a Pixmap file", None, "*.x?m", None)
    xf.fl_do_forms()
    return 0



def load_file(fname, data):

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
                xf.fl_hide_object(fd_ttt.bm)
                xf.fl_free_pixmap_pixmap(fd_ttt.pm)
                xf.fl_set_pixmap_file(fd_ttt.pm, fname)
                xf.fl_show_object(fd_ttt.pm)
            elif fname.endswith(".xbm"):
                xf.fl_hide_object(fd_ttt.pm)
                xf.fl_set_bitmap_file(fd_ttt.bm, fname)
                xf.fl_show_object(fd_ttt.bm)
            else:
                print "Invalid file extension: %s\n" % ext
                return 0

    return 1



def done(pobj, q):
    xf.fl_finish()
    sys.exit(0)



def reloadfile(pobj, q):
    xf.fl_set_fselector_placement(xfc.FL_PLACE_MOUSE)
    xf.fl_set_fselector_callback(load_file, 0)
    xf.fl_show_fselector("Load a Pix/bitMap file", None, None, None)




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

