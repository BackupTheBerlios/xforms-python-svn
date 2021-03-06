#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  demotest2.c XForms demo, with some adaptations.
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
import xformslib as xfl


def timeout_remove_alert(idn, vdata):
    xfl.fl_hide_alert()


def main(lsysargv, sysargv):
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    xfl.fl_set_resource(xfl.FLOKLabel, "Go")
    if xfl.fl_show_question("Do you want bold font ?", 1):
        xfl.fl_set_goodies_font(xfl.FL_BOLD_STYLE, xfl.FL_NORMAL_SIZE)
    xfl.fl_show_messages("This is a test program for the goodies of the " \
            "xforms library")
    xfl.fl_add_timeout(5000, timeout_remove_alert, 0)
    xfl.fl_show_alert("Alert", "Alert form can be used to inform",
            "recoverable errors", 0)
    if xfl.fl_show_question("Do you want to quit?", 0):
        sys.exit(0)
    s = xfl.fl_show_input("Give a string:", "" )
    if s:
        str1 = s
    else:
        str1 = ""
    print(str1, type(str1))
    xfl.fl_show_message("You typed:", "", str1)
    choice = xfl.fl_show_choices("Pick a choice", 2, "One", "Two", \
            "Three", 2)
    if choice == 1:
        xfl.fl_show_message("You typed: One", "", "")
    elif choice == 2:
        xfl.fl_show_message("You typed: Two", "", "")
    elif choice == 3:
        xfl.fl_show_message("You typed: Three", "", "")
    else:
        xfl.fl_show_message("An error occured!", "", "")
    s = xfl.fl_show_input("Give another string:", str1)
    if s:
        str2 = s
    else:
        str2 = "<Cancel>"
    print(str2, type(str2))
    xfl.fl_show_message("You typed:", "", str2)
    xfl.fl_show_messages(str2)
    xfl.fl_finish()
    return 0


if __name__ == '__main__':
    print("********* demotest2.py *********")
    main(len(sys.argv), sys.argv)
