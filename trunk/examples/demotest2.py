#!/usr/bin/env python

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
from xformslib import library as xf
from xformslib import xfdata as xfc




def timeout_remove_alert(idn, vdata):
    xf.fl_hide_alert()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    if 0:
        xf.fl_set_resource(xfc.FLOKLabel, "Go")


    if xf.fl_show_question("Do you want bold font ?", 1):
        xf.fl_set_goodies_font(xfc.FL_BOLD_STYLE, xfc.FL_NORMAL_SIZE)

    xf.fl_show_messages("This is a test program for the goodies of the"
                        "forms library")

    xf.fl_add_timeout(5000, timeout_remove_alert, 0)
    xf.fl_show_alert("Alert", "Alert form can be used to inform",
                     "recoverable errors", 0)

    if xf.fl_show_question("Do you want to quit?", 0):
        sys.exit(0)

    s = xf.fl_show_input("Give a string:", "" )
    if s:
        str1 = s
    else:
        str1 = ""

    xf.fl_show_message("You typed:", "", str1)
    choice = xf.fl_show_choices("Pick a choice", 2, "One", "Two", "Three", 2)

    if choice == 1:
        xf.fl_show_message("You typed: One", "", "")
    elif choice == 2:
        xf.fl_show_message("You typed: Two", "", "")
    elif choice == 3:
        xf.fl_show_message("You typed: Three", "", "")
    else:
        xf.fl_show_message("An error occured!", "", "")

    s = xf.fl_show_input("Give another string:", str1)
    if s:
        str2 = s
    else:
        str2 = "<Cancel>"

    xf.fl_show_message("You typed:", "", str2)
    xf.fl_show_messages("Good Bye")

    xf.fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

