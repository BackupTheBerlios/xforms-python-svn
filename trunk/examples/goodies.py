#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  goodies.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo program uses the routines in the
#   goodies section, that help you create easy
#   forms in an even easier way.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flgoodies import *
from xformslib.xfdata import *




def timeout_remove_alert(idn, data):
    fl_hide_alert()


def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    fl_set_resource(FLOKLabel, "Go")

    if fl_show_question("Do you want bold font ?", 1):
        fl_set_goodies_font(FL_BOLD_STYLE, FL_NORMAL_SIZE)

    fl_show_messages("This is a test program for the goodies of the "
                        "forms library")

    fl_add_timeout(5000, timeout_remove_alert, 0)
    fl_show_alert("Alert", "Alert form can be used to inform", \
                     " about recoverable errors", 0)

    if fl_show_question("Do you want to quit?", 0):
        sys.exit(0)

    s = fl_show_input("Give a string:", "")
    if not s:
        s = ""
    str1 = s
    fl_show_message("You typed:", "", str1)

    choice = fl_show_choices("Pick a choice", 3, "One", "Two", "Three", 2)
    if choice == 1:
        fl_show_message("You typed: One", "", "")
    elif choice == 2:
        fl_show_message("You typed: Two", "", "")
    elif choice == 3:
        fl_show_message("You typed: Three", "", "")
    else:
        fl_show_message("An error occured!", "", "")

    s = fl_show_input("Give another string:", str1)
    if not s:
        s = "<Cancel>"
    str2 = s
    fl_show_message("You typed:", "", str2)
    fl_show_messages("Good Bye")

    fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

