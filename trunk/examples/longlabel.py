#!/usr/bin/env python

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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




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

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = fl_bgn_form(FL_UP_BOX, 400, 300)

    pstrobj = fl_add_box(FL_DOWN_BOX, 10, 10, 380, 240, "Press Next")
    fl_set_object_lsize(pstrobj, FL_NORMAL_SIZE)

    pbut = fl_add_button(FL_NORMAL_BUTTON, 160, 260, 80, 30, "Next")

    fl_end_form()

    fl_set_form_hotobject(pform, pbut)

    fl_show_form(pform, FL_PLACE_HOTSPOT, FL_TRANSIENT, "longlabel")
    fl_do_forms()

    fl_set_object_label(pstrobj, label1)
    fl_do_forms()

    fl_set_object_label(pstrobj, label2)
    fl_do_forms()

    fl_set_object_label(pstrobj, "Now we turn to a short label")
    fl_do_forms()

    fl_set_object_label(pstrobj, label3)
    fl_set_object_label(pbut, "Quit")
    fl_do_forms()

    fl_finish()
    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

