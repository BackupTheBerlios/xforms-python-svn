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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flbitmap import *
from xformslib.flchart import *
from xformslib.flclock import *
from xformslib.flmisc import *
from xformslib.fldial import *
from xformslib.flinput import *
from xformslib.flslider import *
from xformslib.flcounter import *
from xformslib.flpositioner import *
from xformslib.fltabfolder import *
from xformslib.flscrollbar import *
from xformslib.flbrowser import *
from xformslib.flgoodies import *
from xformslib.xfdata import *
from xformslib import deprecated



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



class Flfolder(object):

    def __init__(self, lsysargv, sysargv):

        fl_set_border_width(-2)
        fl_initialize(lsysargv, sysargv, 0, 0, 0)
        self.fd_mainform = self.create_form_mainform()
        fl_set_object_return(self.fd_mainform.folder, FL_RETURN_NONE)

        self.make_folder(self.fd_mainform.folder)

        # show the first form
        fl_show_form(self.fd_mainform.mainform, FL_PLACE_ASPECT, \
                    FL_FULLBORDER, "TabFolder")

        fl_do_forms()


    # callback routines
    def hide_show_cb(self, pobj, data):
        if data:
            fl_show_object(self.fd_mainform.folder)
        else:
            fl_hide_object(self.fd_mainform.folder)


    def reshow_cb(self, pobj, data):
        fl_hide_form(pobj.contents.form)
        fl_show_form(pobj.contents.form, FL_PLACE_POSITION, \
                     FL_FULLBORDER, "TabFolder")


    def set_cb(self, pobj, data):
        n = fl_get_active_folder_number(self.fd_mainform.folder)
        fl_set_folder_bynumber(self.fd_mainform.folder, n % 5 + 1)


    def deactivate_cb(self, pobj, data):
        if fl_object_is_active(self.fd_mainform.folder):
            fl_set_object_label(pobj, "Activate")
            fl_deactivate_object(self.fd_mainform.folder)
        else:
            fl_set_object_label(pobj, "Deactivate")
            fl_activate_object(self.fd_mainform.folder)


    def done_cb(self, pobj, data):

        if fl_show_question("Do you want to quit ?", 0):
            print("will quit after 5 seconds\n")
            fl_msleep(5000)
            fl_hide_form(pobj.contents.form)
            fl_free_form(pobj.contents.form)
            fl_finish()
            sys.exit(0)
        else:
            return 0


    def create_form_buttonform(self):

        fdui = FD_buttonform()

        fdui.buttonform = fl_bgn_form(FL_NO_BOX, 430, 210)

        pobj = fl_add_box(FL_FLAT_BOX, 0, 0, 430, 210, "")

        pobj1 = fl_add_button(FL_NORMAL_BUTTON, 30, 151, \
                           80, 30, "Button")
        fl_set_object_lalign(pobj1, FL_ALIGN_CENTER)

        pobj2 = fl_add_roundbutton(FL_PUSH_BUTTON, 40, 91, \
                                100, 30, "RoundButton")

        pobj3 = fl_add_round3dbutton(FL_PUSH_BUTTON, 135, 151, \
                                  110, 30, "Round3DButton")
        fl_set_object_color(pobj3, FL_COL1, FL_BLUE)

        pobj4 = fl_add_checkbutton(FL_PUSH_BUTTON, 170, 111, \
                                110, 30, "CheckButton")

        pobj4 = fl_add_lightbutton(FL_PUSH_BUTTON, 30, 31, \
                                100, 30, "LightButton")

        pobj5 = fl_add_pixmapbutton(FL_NORMAL_BUTTON, 320, 36, \
                                 80, 80, "PixmapButton")
        fl_set_object_color(pobj5, FL_COL1, FL_YELLOW)
        fl_set_pixmapbutton_file(pobj5, "porsche.xpm")

        pobj6 = fl_add_button(FL_NORMAL_BUTTON, 185, 26, \
                           100, 30, "Button")
        fl_set_object_boxtype(pobj6, FL_ROUNDED3D_UPBOX)
        fl_set_object_lalign(pobj6, FL_ALIGN_CENTER)

        pobj7 = fl_add_lightbutton(FL_PUSH_BUTTON, 290, 146, \
                                100, 30, "Button")
        fl_set_object_boxtype(pobj7, FL_EMBOSSED_BOX)

        pobj8 = fl_add_button(FL_NORMAL_BUTTON, 175, 71, \
                           60, 25, "Button")
        fl_set_object_boxtype(pobj8, FL_SHADOW_BOX)
        fl_set_object_color(pobj8, FL_COL1, FL_SLATEBLUE)
        fl_set_object_lalign(pobj8, FL_ALIGN_CENTER)

        fl_end_form()

        return fdui


    def create_form_staticform(self):

        fdui = FD_staticform()

        fdui.staticform = fl_bgn_form(FL_NO_BOX, 431, 211)

        pobj = fl_add_box(FL_FLAT_BOX, 0, 0, 431, 211, "")
        fl_set_object_color(pobj, FL_INDIANRED, FL_INDIANRED)
        fl_set_object_lcolor(pobj, FL_INDIANRED)

        pobj1 = fl_add_box(FL_UP_BOX, 40, 40, 60, 45, "A Box")

        pobj2 = fl_add_labelframe(FL_ENGRAVED_FRAME, 130, 30, \
                                 120, 55, "LabelFrame")
        fl_set_object_color(pobj2, FL_BLACK, FL_INDIANRED)
        fl_set_object_lstyle(pobj2, FL_BOLD_STYLE)

        fdui.chart = fl_add_chart(FL_PIE_CHART, 270, 20, \
                                 130, 105, "")
        fl_set_object_color(fdui.chart, FL_INDIANRED, FL_COL1)

        pobj3 = fl_add_clock(FL_ANALOG_CLOCK, 30, 100, 85, 85, "")
        fl_set_object_color(pobj3, FL_COL1, FL_RIGHT_BCOL)

        pobj4 = fl_add_bitmap(FL_NORMAL_BITMAP, 150, 140, 30, 25, "")
        fl_set_bitmap_file(pobj4, "srs.xbm")

        pobj5 = fl_add_pixmap(FL_NORMAL_PIXMAP, 210, 120, 60, 60, "")
        fl_set_pixmap_file(pobj5, "porsche.xpm")

        pobj6 = fl_add_text(FL_NORMAL_TEXT, 310, 150, 70, 25, "Text")
        fl_set_object_boxtype(pobj6, FL_BORDER_BOX)

        fl_end_form()

        return fdui


    def create_form_mainform(self):

        fdui = FD_mainform()

        fdui.mainform = fl_bgn_form(FL_NO_BOX, 461, 291)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 461, 291, "")

        fdui.done = fl_add_button(FL_NORMAL_BUTTON, 381, 250, \
                                 64, 25, "Done")
        fl_set_object_lalign(fdui.done, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.done, self.done_cb, 0)

        fdui.hide = fl_add_button(FL_NORMAL_BUTTON, 15, 249, \
                                 64, 27, "Hide")
        fl_set_button_shortcut(fdui.hide, "^H", 1)
        fl_set_object_lalign(fdui.hide, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.hide, self.hide_show_cb, 0)

        fdui.show = fl_add_button(FL_NORMAL_BUTTON, 79, 249, \
                                 64, 27, "Show")
        fl_set_button_shortcut(fdui.show, "^S", 1)
        fl_set_object_lalign(fdui.show, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.show, self.hide_show_cb, 1)

        fdui.reshow = fl_add_button(FL_NORMAL_BUTTON, 155, 249, \
                                         64, 27, "ReShow")
        fl_set_button_shortcut(fdui.reshow, "^R", 1)
        fl_set_object_lalign(fdui.reshow, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.reshow, self.reshow_cb, 0)

        fdui.folder = fl_add_tabfolder(FL_TOP_TABFOLDER, 15, 11, \
                                            435, 230, "")
        fl_set_object_resize(fdui.folder, FL_RESIZE_ALL)

        fdui.set = fl_add_button(FL_NORMAL_BUTTON, 232, 249, \
                                      64, 27, "Set")
        fl_set_object_lalign(fdui.set, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.set, self.set_cb, 0)

        fdui.deactivate = fl_add_button(FL_NORMAL_BUTTON, 296, 249, \
                                       69, 27, "Deactivate")
        fl_set_object_lalign(fdui.deactivate, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.deactivate, self.deactivate_cb, 0)

        fl_end_form()

        return fdui


    def create_form_valuatorform(self):

        fdui = FD_valuatorform()

        fdui.valuatorform = fl_bgn_form(FL_NO_BOX, 431, 211)

        pobj = fl_add_box(FL_FLAT_BOX, 0, 0, 431, 211, "")

        pobj1 = fl_add_positioner(FL_NORMAL_POSITIONER, 280, 50, 82, 72, "")
        fl_set_positioner_xvalue(pobj1, 0.679012)
        fl_set_positioner_yvalue(pobj1, 0.71831)

        pobj2 = fl_add_valslider(FL_HOR_NICE_SLIDER, 55, 10, 240, 20, "")
        fl_set_object_boxtype(pobj2, FL_FLAT_BOX)
        fl_set_object_color(pobj2, FL_COL1, FL_RIGHT_BCOL)
        fl_set_object_return(pobj2, FL_RETURN_CHANGED)
        fl_set_slider_value(pobj2, 0.87)

        pobj3 = fl_add_counter(FL_NORMAL_COUNTER, 130, 110, 110, 20, "")
        fl_set_counter_value(pobj3, -1.0)

        pobj4 = fl_add_slider(FL_VERT_NICE_SLIDER, 10, 30, 20, 160, "")
        fl_set_object_boxtype(pobj4, FL_FLAT_BOX)
        fl_set_object_color(pobj4, FL_COL1, FL_RED)
        fl_set_object_return(pobj4, FL_RETURN_CHANGED)
        fl_set_slider_value(pobj4, 0.49)

        pobj5 = fl_add_valslider(FL_HOR_BROWSER_SLIDER, 70, 170, 150, 21, "")
        fl_set_object_return(pobj5, FL_RETURN_CHANGED)

        pobj6 = fl_add_slider(FL_HOR_FILL_SLIDER, 69, 57, 159, 22, "")
        fl_set_object_color(pobj6, FL_COL1, FL_SLATEBLUE)
        fl_set_object_return(pobj6, FL_RETURN_CHANGED)
        fl_set_slider_value(pobj6, 0.25)

        pobj7 = fl_add_dial(FL_NORMAL_DIAL, 60, 90, 60, 58, "")
        fl_set_object_boxtype(pobj7, FL_UP_BOX)
        fl_set_object_return(pobj7, FL_RETURN_END_CHANGED)

        pobj8 = fl_add_scrollbar(FL_VERT_THIN_SCROLLBAR, 394, 14, 18, 180, "")
        fl_set_object_boxtype(pobj8, FL_DOWN_BOX)
        fl_set_object_resize(pobj8, FL_RESIZE_ALL)
        fl_set_scrollbar_size(pobj8, 0.20)

        pobj9 = fl_add_scrollbar(FL_HOR_SCROLLBAR, 238, 158, 140, 16, "")
        fl_set_object_resize(pobj9, FL_RESIZE_ALL)
        fl_set_scrollbar_size(pobj9, 0.25)

        fl_end_form()

        return fdui


    def create_form_choiceform(self):

        fdui = FD_choiceform()

        fdui.choiceform = fl_bgn_form(FL_NO_BOX, 431, 211)

        pobj = fl_add_box(FL_FLAT_BOX, 0, 0, 431, 211, "")

        fdui.pulldown = deprecated.fl_add_menu(deprecated.FL_PULLDOWN_MENU, 45, 36, \
                                       45, 21, "Menu")
        fl_set_object_color(fdui.pulldown, FL_COL1, FL_LEFT_BCOL)
        fl_set_object_lstyle(fdui.pulldown, FL_BOLD_STYLE)

        fdui.choice = deprecated.fl_add_choice(deprecated.FL_NORMAL_CHOICE2, 24, 93, \
                                       111, 27, "")

        fdui.browser = fl_add_browser(FL_HOLD_BROWSER, 257, 14, 154, 179, "")
        fl_set_object_color(fdui.browser, FL_COL1, FL_YELLOW)

        fdui.pushmenu = deprecated.fl_add_menu(deprecated.FL_PUSH_MENU, 152, 51, \
                                       75, 26, "Menu")
        fl_set_object_boxtype(fdui.pushmenu, FL_UP_BOX)
        fl_set_object_lstyle(fdui.pushmenu, FL_BOLD_STYLE)

        fl_end_form()

        return fdui


    def create_form_inputform(self):

        fdui = FD_inputform()

        fdui.inputform = fl_bgn_form(FL_NO_BOX, 430, 210)

        pobj = fl_add_box(FL_FLAT_BOX, 0, 0, 430, 210, "")

        pobj1 = fl_add_input(FL_MULTILINE_INPUT, 70, 20, 280, 90, "MultiLine\nInput")
        fl_set_object_return(pobj1, FL_RETURN_ALWAYS)

        pobj2 = fl_add_input(FL_NORMAL_INPUT, 80, 132, 250, 34, "Input")
        fl_set_object_return(pobj2, FL_RETURN_END_CHANGED)

        fl_end_form()

        return fdui


    def make_folder(self, folder):
        x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        y = [5.5, 4, 4.5, 3.8, 4, 5]
        label = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

        fd_buttonform = self.create_form_buttonform()
        fd_staticform = self.create_form_staticform()
        fd_valuatorform = self.create_form_valuatorform()
        fd_choiceform = self.create_form_choiceform()
        fd_inputform = self.create_form_inputform()

        # fill-in form initialization code

        for i in range (0, len(y)):
            fl_add_chart_value(fd_staticform.chart, y[i], label[i], i + 1)

        deprecated.fl_addto_menu(fd_choiceform.pulldown, \
                    "MenuEntry1|MenuEntry2|MenuEntry3|MenuEntry4")
        deprecated.fl_addto_menu(fd_choiceform.pushmenu, \
                     "MenuEntry1|MenuEntry2|MenuEntry3")
        deprecated.fl_addto_choice(fd_choiceform.choice, \
                       "Choice1|Choice2|Choice3|Choice4|Choice5|Choice6")

        fl_load_browser(fd_choiceform.browser, "Readme")

        fl_addto_tabfolder(folder, "ButtonObj", fd_buttonform.buttonform)
        fl_addto_tabfolder(folder, "StaticObj", fd_staticform.staticform)
        fl_addto_tabfolder(folder, "ValuatorObj", fd_valuatorform.valuatorform)
        fl_addto_tabfolder(folder, "ChoiceObj", fd_choiceform.choiceform)
        fl_addto_tabfolder(folder, "InputObj", fd_inputform.inputform)




if __name__ == '__main__':
    Flfolder(len(sys.argv), sys.argv)

