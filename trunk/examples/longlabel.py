#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  longlabel.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo of the Use of a very long label
#

import sys
#sys.path.append("..")
import xformslib as xfl


label1 = "This demo shows the use of some very\n" \
         "long labels. The dynamic storage allocation\n" \
         "for such long labels should guarantee that\n" \
         "all of this works without any problem."
label2 = "This is the second string that should again\n" \
         "be a bit larger such that a new, larger amount\n" \
         "of storage has to be allocated for the label.\n" \
         "This is of course no problem. By the way,\n" \
         "dynamic allocation of storage saves a lot\n" \
         "of memory because for most objects the label\n" \
         "is much shorter than the 64 bytes that were\n" \
         "allocated for it in the previous version of\n" \
         "the Forms Library"
label3 = "And now back to the first one:\n\n" \
         "This demo shows the use of some very\n" \
         "long labels. The dynamic storage allocation\n" \
         "for such long labels should guarantee that\n" \
         "all of this works without any problem."


def main(lsysargv, sysargv):
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 300)
    pstrobj = xfl.fl_add_box(xfl.FL_DOWN_BOX, 10, 10, 380, 240, "Press Next")
    xfl.fl_set_object_lsize(pstrobj, xfl.FL_NORMAL_SIZE)
    pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 160, 260, 80, 30, "Next")
    xfl.fl_end_form()
    xfl.fl_set_form_hotobject(pform, pbut)
    xfl.fl_show_form(pform, xfl.FL_PLACE_HOTSPOT, xfl.FL_TRANSIENT, \
            "longlabel")
    xfl.fl_do_forms()
    xfl.fl_set_object_label(pstrobj, label1)
    xfl.fl_do_forms()
    xfl.fl_set_object_label(pstrobj, label2)
    xfl.fl_do_forms()
    xfl.fl_set_object_label(pstrobj, "Now we turn to a short label")
    xfl.fl_do_forms()
    xfl.fl_set_object_label(pstrobj, label3)
    xfl.fl_set_object_label(pbut, "Quit")
    xfl.fl_do_forms()
    xfl.fl_finish()
    return 0


if __name__ == '__main__':
    print("********* longlabel.py *********")
    main(len(sys.argv), sys.argv)
