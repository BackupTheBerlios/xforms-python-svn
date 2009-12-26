#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  folder.c XForms demo, with some adaptation.
#
#  folder.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Tabbed folder demo and tester
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


global fdui

# Forms and Objects
class genericform(object):
    vdata = None
    cdata = ""
    ldata = 0

class FD_buttonform(genericform):
    buttonform = None

class FD_staticform(genericform):
    staticform = None
    chart = None

class FD_mainform(genericform):
    mainform = None
    done = None
    hide = None
    show = None
    reshow = None
    folder = None
    set = None
    deactivate = None

class FD_valuatorform(genericform):
    valuatorform = None

class FD_choiceform(genericform):
    choiceform = None
    pulldown = None
    choice = None
    browser = None
    pushmenu = None

class FD_inputform(genericform):
    inputform = None



# callback routines

def hide_show_cb(ob, data):

    if data:
        xf.fl_show_object(fdui.folder)
    else:
        xf.fl_hide_object(fdui.folder)


def reshow_cb(ob, data):
    xf.fl_hide_form(ob[0].form[0])
    xf.fl_show_form(ob[0].form[0], xfc.FL_PLACE_POSITION, \
                    xfc.FL_FULLBORDER, "TabFolder")


def set_cb(ob, data):
    n = xf.fl_get_active_folder_number(fdui.folder)
    xf.fl_set_folder_bynumber(fdui.folder, n % 5 + 1)


def deactivate_cb(ob, data):
    if fdui.folder[0].active:
        xf.fl_set_object_label(ob, "Activate")
        xf.fl_deactivate_object(fdui.folder)
    else:
        xf.fl_set_object_label(ob, "Deactivate")
        xf.fl_activate_object(fdui.folder)



def done_cb(ob, data):

    if xf.fl_show_question("Do you want to quit ?", 0):
        print("will quit after 5 seconds\n")
        xf.fl_msleep(5000)
        xf.fl_hide_form(ob[0].form[0])
        xf.fl_free_form(ob[0].form[0])
        xf.fl_finish()
        sys.exit(0)
    else:
        return 0



def create_form_buttonform():

    fdui = FD_buttonform()

    fdui.buttonform = xf.fl_bgn_form(xfc.FL_NO_BOX, 430, 210)

    obj = xf.fl_add_box(xfc.FL_FLAT_BOX, 0, 0, 430, 210, "")

    obj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 30, 151, \
                           80, 30, "Button")
    xf.fl_set_object_lalign(obj1, xfc.FL_ALIGN_CENTER)

    obj2 = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 40, 91, \
                                100, 30, "RoundButton")

    obj3 = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 135, 151, \
                                  110, 30, "Round3DButton")
    xf.fl_set_object_color(obj3, xfc.FL_COL1, xfc.FL_BLUE)

    obj4 = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 170, 111, \
                                110, 30, "CheckButton")

    obj4 = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 30, 31, \
                                100, 30, "LightButton")

    obj5 = xf.fl_add_pixmapbutton(xfc.FL_NORMAL_BUTTON, 320, 36, \
                                 80, 80, "PixmapButton")
    xf.fl_set_object_color(obj5, xfc.FL_COL1, xfc.FL_YELLOW)
    xf.fl_set_pixmapbutton_file(obj5, "porsche.xpm")

    obj6 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 185, 26, \
                           100, 30, "Button")
    xf.fl_set_object_boxtype(obj6, xfc.FL_ROUNDED3D_UPBOX)
    xf.fl_set_object_lalign(obj6, xfc.FL_ALIGN_CENTER)

    obj7 = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 290, 146, \
                                100, 30, "Button")
    xf.fl_set_object_boxtype(obj7, xfc.FL_EMBOSSED_BOX)

    obj8 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 175, 71, \
                           60, 25, "Button")
    xf.fl_set_object_boxtype(obj8, xfc.FL_SHADOW_BOX)
    xf.fl_set_object_color(obj8, xfc.FL_COL1, xfc.FL_SLATEBLUE)
    xf.fl_set_object_lalign(obj8, xfc.FL_ALIGN_CENTER)

    xf.fl_end_form()

    return fdui



def create_form_staticform():

    fdui = FD_staticform()

    fdui.staticform = xf.fl_bgn_form(xfc.FL_NO_BOX, 431, 211)

    obj = xf.fl_add_box(xfc.FL_FLAT_BOX, 0, 0, 431, 211, "")
    xf.fl_set_object_color(obj, xfc.FL_INDIANRED, xfc.FL_INDIANRED)
    xf.fl_set_object_lcolor(obj, xfc.FL_INDIANRED)

    obj1 = xf.fl_add_box(xfc.FL_UP_BOX, 40, 40, 60, 45, "A Box")

    obj2 = xf.fl_add_labelframe(xfc.FL_ENGRAVED_FRAME, 130, 30, \
                                120, 55, "LabelFrame")
    xf.fl_set_object_color(obj2, xfc.FL_BLACK, xfc.FL_INDIANRED)
    xf.fl_set_object_lstyle(obj2, xfc.FL_BOLD_STYLE)

    fdui.chart = xf.fl_add_chart(xfc.FL_PIE_CHART, 270, 20, \
                                 130, 105, "")
    xf.fl_set_object_color(fdui.chart, xfc.FL_INDIANRED, xfc.FL_COL1)

    obj3 = xf.fl_add_clock(xfc.FL_ANALOG_CLOCK, 30, 100, 85, 85, "")
    xf.fl_set_object_color(obj3, xfc.FL_COL1, xfc.FL_RIGHT_BCOL)

    obj4 = xf.fl_add_bitmap(xfc.FL_NORMAL_BITMAP, 150, 140, 30, 25, "")
    xf.fl_set_bitmap_file(obj4, "srs.xbm")

    obj5 = xf.fl_add_pixmap(xfc.FL_NORMAL_PIXMAP, 210, 120, 60, 60, "")
    xf.fl_set_pixmap_file(obj5, "porsche.xpm")

    obj6 = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 310, 150, 70, 25, "Text")
    xf.fl_set_object_boxtype(obj6, xfc.FL_BORDER_BOX)

    xf.fl_end_form()

    return fdui



def create_form_mainform():
    global fdui

    fdui = FD_mainform()

    fdui.mainform = xf.fl_bgn_form(xfc.FL_NO_BOX, 461, 291)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 461, 291, "")

    fdui.done = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 381, 250, \
                                 64, 25, "Done")
    xf.fl_set_object_lalign(fdui.done, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.done, done_cb, 0)

    fdui.hide = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 15, 249, \
                                 64, 27, "Hide")
    xf.fl_set_button_shortcut(fdui.hide, "^H", 1)
    xf.fl_set_object_lalign(fdui.hide, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.hide, hide_show_cb, 0)

    fdui.show = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 79, 249, \
                                 64, 27, "Show")
    xf.fl_set_button_shortcut(fdui.show, "^S", 1)
    xf.fl_set_object_lalign(fdui.show, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.show, hide_show_cb, 1)

    fdui.reshow = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 155, 249, \
                                         64, 27, "ReShow")
    xf.fl_set_button_shortcut(fdui.reshow, "^R", 1)
    xf.fl_set_object_lalign(fdui.reshow, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.reshow, reshow_cb, 0)

    fdui.folder = xf.fl_add_tabfolder(xfc.FL_TOP_TABFOLDER, 15, 11, \
                                            435, 230, "")
    xf.fl_set_object_resize(fdui.folder, xfc.FL_RESIZE_ALL)

    fdui.set = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 232, 249, \
                                      64, 27, "Set")
    xf.fl_set_object_lalign(fdui.set, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.set, set_cb, 0)

    fdui.deactivate = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 296, 249, \
                                       69, 27, "Deactivate")
    xf.fl_set_object_lalign(fdui.deactivate, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.deactivate, deactivate_cb, 0)

    xf.fl_end_form()

    return fdui



def create_form_valuatorform():

    fdui = FD_valuatorform()

    fdui.valuatorform = xf.fl_bgn_form(xfc.FL_NO_BOX, 431, 211)

    obj = xf.fl_add_box(xfc.FL_FLAT_BOX, 0, 0, 431, 211, "")

    obj1 = xf.fl_add_positioner(xfc.FL_NORMAL_POSITIONER, 280, 50, 82, 72, "")
    xf.fl_set_positioner_xvalue(obj1, 0.679012)
    xf.fl_set_positioner_yvalue(obj1, 0.71831)

    obj2 = xf.fl_add_valslider(xfc.FL_HOR_NICE_SLIDER, 55, 10, 240, 20, "")
    xf.fl_set_object_boxtype(obj2, xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(obj2, xfc.FL_COL1, xfc.FL_RIGHT_BCOL)
    xf.fl_set_object_return(obj2, xfc.FL_RETURN_CHANGED)
    xf.fl_set_slider_value(obj2, 0.87)

    obj3 = xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 130, 110, 110, 20, "")
    xf.fl_set_counter_value(obj3, -1.0)

    obj4 = xf.fl_add_slider(xfc.FL_VERT_NICE_SLIDER, 10, 30, 20, 160, "")
    xf.fl_set_object_boxtype(obj4, xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(obj4, xfc.FL_COL1, xfc.FL_RED)
    xf.fl_set_object_return(obj4, xfc.FL_RETURN_CHANGED)
    xf.fl_set_slider_value(obj4, 0.49)

    obj5 = xf.fl_add_valslider(xfc.FL_HOR_BROWSER_SLIDER, 70, 170, 150, 21, "")
    xf.fl_set_object_return(obj5, xfc.FL_RETURN_CHANGED)

    obj6 = xf.fl_add_slider(xfc.FL_HOR_FILL_SLIDER, 69, 57, 159, 22, "")
    xf.fl_set_object_color(obj6, xfc.FL_COL1, xfc.FL_SLATEBLUE)
    xf.fl_set_object_return(obj6, xfc.FL_RETURN_CHANGED)
    xf.fl_set_slider_value(obj6, 0.25)

    obj7 = xf.fl_add_dial(xfc.FL_NORMAL_DIAL, 60, 90, 60, 58, "")
    xf.fl_set_object_boxtype(obj7, xfc.FL_UP_BOX)
    xf.fl_set_object_return(obj7, xfc.FL_RETURN_END_CHANGED)

    obj8 = xf.fl_add_scrollbar(xfc.FL_VERT_THIN_SCROLLBAR, 394, 14, 18, 180, "")
    xf.fl_set_object_boxtype(obj8, xfc.FL_DOWN_BOX)
    xf.fl_set_object_resize(obj8, xfc.FL_RESIZE_ALL)
    xf.fl_set_scrollbar_size(obj8, 0.20)

    obj9 = xf.fl_add_scrollbar(xfc.FL_HOR_SCROLLBAR, 238, 158, 140, 16, "")
    xf.fl_set_object_resize(obj9, xfc.FL_RESIZE_ALL)
    xf.fl_set_scrollbar_size(obj9, 0.25)

    xf.fl_end_form()

    return fdui



def create_form_choiceform():

    fdui = FD_choiceform()

    fdui.choiceform = xf.fl_bgn_form(xfc.FL_NO_BOX, 431, 211)

    obj = xf.fl_add_box(xfc.FL_FLAT_BOX, 0, 0, 431, 211, "")

    fdui.pulldown = xf.fl_add_menu(xfc.FL_PULLDOWN_MENU, 45, 36, \
                                         45, 21, "Menu")
    xf.fl_set_object_color(fdui.pulldown, xfc.FL_COL1, xfc.FL_LEFT_BCOL)
    xf.fl_set_object_lstyle(fdui.pulldown, xfc.FL_BOLD_STYLE)

    fdui.choice = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE2, 24, 93, 111, 27, "")

    fdui.browser = xf.fl_add_browser(xfc.FL_HOLD_BROWSER, 257, 14, 154, 179, "")
    xf.fl_set_object_color(fdui.browser, xfc.FL_COL1, xfc.FL_YELLOW)

    fdui.pushmenu = xf.fl_add_menu(xfc.FL_PUSH_MENU, 152, 51, 75, 26, "Menu")
    xf.fl_set_object_boxtype(fdui.pushmenu, xfc.FL_UP_BOX)
    xf.fl_set_object_lstyle(fdui.pushmenu, xfc.FL_BOLD_STYLE)

    xf.fl_end_form()

    return fdui



def create_form_inputform():

    fdui = FD_inputform()

    fdui.inputform = xf.fl_bgn_form(xfc.FL_NO_BOX, 430, 210)

    obj = xf.fl_add_box(xfc.FL_FLAT_BOX, 0, 0, 430, 210, "")

    obj1 = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 70, 20, 280, 90, "MultiLine\nInput")
    xf.fl_set_object_return(obj1, xfc.FL_RETURN_ALWAYS)

    obj2 = xf.fl_add_input(xfc.FL_NORMAL_INPUT, 80, 132, 250, 34, "Input")
    xf.fl_set_object_return(obj2, xfc.FL_RETURN_END_CHANGED)

    xf.fl_end_form()

    return fdui



def make_folder(folder):

    x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    y = [5.5, 4, 4.5, 3.8, 4, 5]
    label = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

    fd_buttonform = create_form_buttonform()
    fd_staticform = create_form_staticform()
    fd_valuatorform = create_form_valuatorform()
    fd_choiceform = create_form_choiceform()
    fd_inputform = create_form_inputform()

    # fill-in form initialization code

    for i in range (0, len(y)):
        xf.fl_add_chart_value(fd_staticform.chart, y[i], label[i], i + 1)
    xf.fl_addto_menu(fd_choiceform.pulldown, \
                    "MenuEntry1|MenuEntry2|MenuEntry3|MenuEntry4")
    xf.fl_addto_menu(fd_choiceform.pushmenu, \
                     "MenEntry1|MenuEntry2|MenuEntry3")
    xf.fl_addto_choice(fd_choiceform.choice, \
                       "Choice1|Choice2|Choice3|Choice4|Choice5|Choice6")

    xf.fl_load_browser(fd_choiceform.browser, "Readme")

    xf.fl_addto_tabfolder(folder,"ButtonObj", fd_buttonform.buttonform)
    xf.fl_addto_tabfolder(folder,"StaticObj", fd_staticform.staticform)
    xf.fl_addto_tabfolder(folder,"ValuatorObj", fd_valuatorform.valuatorform)
    xf.fl_addto_tabfolder(folder,"ChoiceObj", fd_choiceform.choiceform)
    xf.fl_addto_tabfolder(folder,"InputObj", fd_inputform.inputform)



def main(lsysargv, sysargv):

    xf.fl_set_border_width(-2)
    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_mainform = create_form_mainform()
    xf.fl_set_object_return(fd_mainform.folder, xfc.FL_RETURN_NONE)

    make_folder(fd_mainform.folder)

    # show the first form
    xf.fl_show_form(fd_mainform.mainform, xfc.FL_PLACE_ASPECT, \
                    xfc.FL_FULLBORDER, "TabFolder")

    xf.fl_do_forms()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

