#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  dirlist.c XForms demo, with some adaptations.
#
#  dirlist.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# test of fl_get_dirlist() and its kin.
#

import sys
#sys.path.append("..")
import xformslib as xfl



# Forms and Objects
class FD_fbform(object):
    fbform = None
    vdata = None
    cdata = ""
    ldata = 0
    browser = None
    total = None


def fill_browser(pobj):

    nfiles = 0
    dl, nfiles = xfl.fl_get_dirlist( ".", "*", 0)
    #	const FL_Dirlist *ds;
    #const FL_Dirlist *dlend = dl + nfiles;
    xfl.fl_freeze_form(pobj.contents.form)
    buf = "Total %d files" % nfiles
    xfl.fl_set_object_label(fd_fbform.total, buf)
    xfl.fl_clear_browser(fd_fbform.browser)

    #for ( ds = dl; dl < dlend; dl++ )
    for ds in range(0, nfiles):
        #sprintf(buf, "%-10s\t\t%5ldK\t%s", dl->name, dl->dl_size >> 10,
        #         ctime( &dl->dl_mtime ) + 3)
        buf = "%-10s\t%5ldK\t%s\n" % (dl[ds].name, \
                dl[ds].dl_size >> 10, dl[ds].dl_mtime)
        xfl.fl_addto_browser_chars(fd_fbform.browser, buf)
    xfl.fl_unfreeze_form(pobj.contents.form)

    #xfl.fl_free_dirlist(ds)


# callbacks and freeobj handles for form fbform

def sort_method_cb(pobj, data):
    xfl.fl_set_dirlist_sort(data)
    fill_browser(pobj)


def done_cb(pobj, data):

    xfl.fl_finish()
    sys.exit(0)


def main(lsysargv, sysargv):
    global fd_fbform
    xfl.fl_initialize(lsysargv, sysargv, "", None, 0)
    fd_fbform = create_form_fbform()
    xfl.fl_set_browser_fontstyle(fd_fbform.browser, xfl.FL_FIXED_STYLE)

    # fill-in form initialization code
    fill_browser(fd_fbform.browser)

    # show the first form
    xfl.fl_show_form(fd_fbform.fbform, xfl.FL_PLACE_CENTERFREE, \
            xfl.FL_FULLBORDER, "fbform")

    xfl.fl_do_forms()

    return 0


def create_form_fbform():

    fdui = FD_fbform()

    fdui.vdata = fdui.cdata = None
    fdui.ldata = 0

    fdui.fbform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 371, 361)

    pobj = xfl.fl_add_box( xfl.FL_UP_BOX, 0, 0, 371, 361, "")

    fdui.browser = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 20, 50, 240, 290, "")
    xfl.fl_set_object_color(fdui.browser, xfl.FL_COL1, xfl.FL_YELLOW)

    pobj = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 270, 50, 70, 25, "AlphaSort")
    xfl.fl_set_object_callback(pobj, sort_method_cb, xfl.FL_ALPHASORT)
    xfl.fl_set_button(pobj, 1)

    pobj = xfl.fl_add_checkbutton( xfl.FL_RADIO_BUTTON, 270, 85, 70, 25, "SizeSort")
    xfl.fl_set_object_callback(pobj, sort_method_cb, xfl.FL_SIZESORT)

    pobj = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 270, 120, 70, 25, "TimeSort")
    xfl.fl_set_object_callback(pobj, sort_method_cb, xfl.FL_MTIMESORT)

    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 275, 310, 75, 25, "Done")
    xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
    xfl.fl_set_object_callback(pobj, done_cb, 0)

    fdui.total = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 10, 15, 220, 30, "")
    xfl.fl_set_object_boxtype(fdui.total, xfl.FL_NO_BOX)

    xfl.fl_end_form()

    return fdui



if __name__ == '__main__':
    print("********* dirlist.py *********")
    main(len(sys.argv), sys.argv)

