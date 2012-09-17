#!/usr/bin/env python3

#  This file is part of xforms-python, and it is a variant of
#  folder.c XForms demo, not using deprecated functions, with some
#  adaptations.
#
#  folder.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Tabbed folder demo and tester
#

import sys
#sys.path.append("..")
import xformslib as xfl


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
        xfl.fl_set_border_width(-2)
        xfl.fl_initialize(lsysargv, sysargv, 'FormDemo', 0, 0)
        self.fd_mainform = self.create_form_mainform()
        xfl.fl_set_object_return(self.fd_mainform.folder, xfl.FL_RETURN_NONE)
        self.make_folder(self.fd_mainform.folder)
        # show the first form
        xfl.fl_show_form(self.fd_mainform.mainform, xfl.FL_PLACE_ASPECT, \
                xfl.FL_FULLBORDER, "TabFolder")
        xfl.fl_do_forms()

    # callback routines

    def hide_show_cb(self, pobj, data):
        if data:
            xfl.fl_show_object(self.fd_mainform.folder)
        else:
            xfl.fl_hide_object(self.fd_mainform.folder)


    def reshow_cb(self, pobj, data):
        xfl.fl_hide_form(pobj.contents.form)
        xfl.fl_show_form(pobj.contents.form, xfl.FL_PLACE_POSITION, \
                xfl.FL_FULLBORDER, "TabFolder")


    def set_cb(self, pobj, data):
        n = xfl.fl_get_active_folder_number(self.fd_mainform.folder)
        xfl.fl_set_folder_bynumber(self.fd_mainform.folder, n % 5 + 1)


    def deactivate_cb(self, pobj, data):
        if xfl.fl_object_is_active(self.fd_mainform.folder):
            xfl.fl_set_object_label(pobj, "Activate")
            xfl.fl_deactivate_object(self.fd_mainform.folder)
        else:
            xfl.fl_set_object_label(pobj, "Deactivate")
            xfl.fl_activate_object(self.fd_mainform.folder)


    def done_cb(self, pobj, data):
        if xfl.fl_show_question("Do you want to quit ?", 0):
            print("will quit after 5 seconds\n")
            xfl.fl_msleep(5000)
            xfl.fl_hide_form(pobj.contents.form)
            xfl.fl_free_form(pobj.contents.form)
            xfl.fl_finish()
            sys.exit(0)
        else:
            return 0


    def create_form_buttonform(self):
        fdui = FD_buttonform()
        fdui.buttonform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 430, 210)
        pobj = xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 430, 210, "")
        pobj1 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 30, 151, \
                80, 30, "Button")
        xfl.fl_set_object_lalign(pobj1, xfl.FL_ALIGN_CENTER)
        pobj2 = xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 40, 91, \
                100, 30, "RoundButton")
        pobj3 = xfl.fl_add_round3dbutton(xfl.FL_PUSH_BUTTON, 135, 151, \
                110, 30, "Round3DButton")
        xfl.fl_set_object_color(pobj3, xfl.FL_COL1, xfl.FL_BLUE)
        pobj4 = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 170, 111, \
                110, 30, "CheckButton")
        pobj4 = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 30, 31, \
                100, 30, "LightButton")
        pobj5 = xfl.fl_add_pixmapbutton(xfl.FL_NORMAL_BUTTON, 320, 36, \
                80, 80, "PixmapButton")
        xfl.fl_set_object_color(pobj5, xfl.FL_COL1, xfl.FL_YELLOW)
        xfl.fl_set_pixmapbutton_file(pobj5, "porsche.xpm")
        pobj6 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 185, 26, \
                100, 30, "Button")
        xfl.fl_set_object_boxtype(pobj6, xfl.FL_ROUNDED3D_UPBOX)
        xfl.fl_set_object_lalign(pobj6, xfl.FL_ALIGN_CENTER)
        pobj7 = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 290, 146, \
                100, 30, "Button")
        xfl.fl_set_object_boxtype(pobj7, xfl.FL_EMBOSSED_BOX)
        pobj8 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 175, 71, \
                60, 25, "Button")
        xfl.fl_set_object_boxtype(pobj8, xfl.FL_SHADOW_BOX)
        xfl.fl_set_object_color(pobj8, xfl.FL_COL1, xfl.FL_SLATEBLUE)
        xfl.fl_set_object_lalign(pobj8, xfl.FL_ALIGN_CENTER)
        xfl.fl_end_form()
        return fdui


    def create_form_staticform(self):
        fdui = FD_staticform()
        fdui.staticform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 431, 211)
        pobj = xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 431, 211, "")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_INDIANRED)
        xfl.fl_set_object_lcolor(pobj, xfl.FL_INDIANRED)
        pobj1 = xfl.fl_add_box(xfl.FL_UP_BOX, 40, 40, 60, 45, "A Box")
        pobj2 = xfl.fl_add_labelframe(xfl.FL_ENGRAVED_FRAME, 130, 30, \
                120, 55, "LabelFrame")
        xfl.fl_set_object_color(pobj2, xfl.FL_BLACK, xfl.FL_INDIANRED)
        xfl.fl_set_object_lstyle(pobj2, xfl.FL_BOLD_STYLE)
        fdui.chart = xfl.fl_add_chart(xfl.FL_PIE_CHART, 270, 20, \
                130, 105, "")
        xfl.fl_set_object_color(fdui.chart, xfl.FL_INDIANRED, xfl.FL_COL1)
        pobj3 = xfl.fl_add_clock(xfl.FL_ANALOG_CLOCK, 30, 100, 85, 85, "")
        xfl.fl_set_object_color(pobj3, xfl.FL_COL1, xfl.FL_RIGHT_BCOL)
        pobj4 = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 150, 140, 30, 25, "")
        xfl.fl_set_bitmap_file(pobj4, "srs.xbm")
        pobj5 = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 210, 120, 60, 60, "")
        xfl.fl_set_pixmap_file(pobj5, "porsche.xpm")
        pobj6 = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 310, 150, 70, 25, "Text")
        xfl.fl_set_object_boxtype(pobj6, xfl.FL_BORDER_BOX)
        xfl.fl_end_form()
        return fdui


    def create_form_mainform(self):
        fdui = FD_mainform()
        fdui.mainform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 461, 291)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 461, 291, "")
        fdui.done = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 381, 250, \
                64, 25, "Done")
        xfl.fl_set_object_lalign(fdui.done, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.done, self.done_cb, 0)
        fdui.hide = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 15, 249, \
                64, 27, "Hide")
        xfl.fl_set_button_shortcut(fdui.hide, "^H", 1)
        xfl.fl_set_object_lalign(fdui.hide, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.hide, self.hide_show_cb, 0)
        fdui.show = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 79, 249, \
                64, 27, "Show")
        xfl.fl_set_button_shortcut(fdui.show, "^S", 1)
        xfl.fl_set_object_lalign(fdui.show, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.show, self.hide_show_cb, 1)
        fdui.reshow = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 155, 249, \
                64, 27, "ReShow")
        xfl.fl_set_button_shortcut(fdui.reshow, "^R", 1)
        xfl.fl_set_object_lalign(fdui.reshow, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.reshow, self.reshow_cb, 0)
        fdui.folder = xfl.fl_add_tabfolder(xfl.FL_TOP_TABFOLDER, 15, 11, \
                435, 230, "")
        xfl.fl_set_object_resize(fdui.folder, xfl.FL_RESIZE_ALL)
        fdui.set = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 232, 249, \
                64, 27, "Set")
        xfl.fl_set_object_lalign(fdui.set, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.set, self.set_cb, 0)
        fdui.deactivate = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 296, 249, \
                69, 27, "Deactivate")
        xfl.fl_set_object_lalign(fdui.deactivate, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.deactivate, self.deactivate_cb, 0)
        xfl.fl_end_form()
        return fdui


    def create_form_valuatorform(self):
        fdui = FD_valuatorform()
        fdui.valuatorform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 431, 211)
        pobj = xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 431, 211, "")
        pobj1 = xfl.fl_add_positioner(xfl.FL_NORMAL_POSITIONER, 280, 50, \
                82, 72, "")
        xfl.fl_set_positioner_xvalue(pobj1, 0.679012)
        xfl.fl_set_positioner_yvalue(pobj1, 0.71831)
        pobj2 = xfl.fl_add_valslider(xfl.FL_HOR_NICE_SLIDER, 55, 10, \
                240, 20, "")
        xfl.fl_set_object_boxtype(pobj2, xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(pobj2, xfl.FL_COL1, xfl.FL_RIGHT_BCOL)
        xfl.fl_set_object_return(pobj2, xfl.FL_RETURN_CHANGED)
        xfl.fl_set_slider_value(pobj2, 0.87)
        pobj3 = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 130, 110, \
                110, 20, "")
        xfl.fl_set_counter_value(pobj3, -1.0)
        pobj4 = xfl.fl_add_slider(xfl.FL_VERT_NICE_SLIDER, 10, 30, \
                20, 160, "")
        xfl.fl_set_object_boxtype(pobj4, xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(pobj4, xfl.FL_COL1, xfl.FL_RED)
        xfl.fl_set_object_return(pobj4, xfl.FL_RETURN_CHANGED)
        xfl.fl_set_slider_value(pobj4, 0.49)
        pobj5 = xfl.fl_add_valslider(xfl.FL_HOR_BROWSER_SLIDER, 70, 170, \
                150, 21, "")
        xfl.fl_set_object_return(pobj5, xfl.FL_RETURN_CHANGED)
        pobj6 = xfl.fl_add_slider(xfl.FL_HOR_FILL_SLIDER, 69, 57, 159, 22, "")
        xfl.fl_set_object_color(pobj6, xfl.FL_COL1, xfl.FL_SLATEBLUE)
        xfl.fl_set_object_return(pobj6, xfl.FL_RETURN_CHANGED)
        xfl.fl_set_slider_value(pobj6, 0.25)
        pobj7 = xfl.fl_add_dial(xfl.FL_NORMAL_DIAL, 60, 90, 60, 58, "")
        xfl.fl_set_object_boxtype(pobj7, xfl.FL_UP_BOX)
        xfl.fl_set_object_return(pobj7, xfl.FL_RETURN_END_CHANGED)
        pobj8 = xfl.fl_add_scrollbar(xfl.FL_VERT_THIN_SCROLLBAR, 394, 14, \
                18, 180, "")
        xfl.fl_set_object_boxtype(pobj8, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_resize(pobj8, xfl.FL_RESIZE_ALL)
        xfl.fl_set_scrollbar_size(pobj8, 0.20)
        pobj9 = xfl.fl_add_scrollbar(xfl.FL_HOR_SCROLLBAR, 238, 158, \
                140, 16, "")
        xfl.fl_set_object_resize(pobj9, xfl.FL_RESIZE_ALL)
        xfl.fl_set_scrollbar_size(pobj9, 0.25)
        xfl.fl_end_form()
        return fdui


    def create_form_choiceform(self):
        fdui = FD_choiceform()
        fdui.choiceform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 431, 211)
        pobj = xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 431, 211, "")
        fdui.pulldown = xfl.fl_add_nmenu(xfl.FL_NORMAL_NMENU, 45, 36, \
                45, 21, "Menu")
        xfl.fl_set_object_color(fdui.pulldown, xfl.FL_COL1, xfl.FL_LEFT_BCOL)
        xfl.fl_set_object_lstyle(fdui.pulldown, xfl.FL_BOLD_STYLE)
        fdui.choice = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 24, 93, \
                111, 27, "")
        fdui.browser = xfl.fl_add_browser(xfl.FL_HOLD_BROWSER, 257, 14, \
                154, 179, "")
        xfl.fl_set_object_color(fdui.browser, xfl.FL_COL1, xfl.FL_YELLOW)
        fdui.pushmenu = xfl.fl_add_nmenu(xfl.FL_BUTTON_NMENU, 152, 51, \
                75, 26, "Menu")
        xfl.fl_set_object_boxtype(fdui.pushmenu, xfl.FL_UP_BOX)
        xfl.fl_set_object_lstyle(fdui.pushmenu, xfl.FL_BOLD_STYLE)
        xfl.fl_end_form()
        return fdui


    def create_form_inputform(self):
        fdui = FD_inputform()
        fdui.inputform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 430, 210)
        pobj = xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 430, 210, "")
        pobj1 = xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 70, 20, 280, 90, \
                "MultiLine\nInput")
        xfl.fl_set_object_return(pobj1, xfl.FL_RETURN_ALWAYS)
        pobj2 = xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 80, 132, 250, 34, \
                "Input")
        xfl.fl_set_object_return(pobj2, xfl.FL_RETURN_END_CHANGED)
        xfl.fl_end_form()
        return fdui


    def make_folder(self, folder):
        #x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        y = [5.5, 4, 4.5, 3.8, 4, 5]
        label = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
        fd_buttonform = self.create_form_buttonform()
        fd_staticform = self.create_form_staticform()
        fd_valuatorform = self.create_form_valuatorform()
        fd_choiceform = self.create_form_choiceform()
        fd_inputform = self.create_form_inputform()
        # fill-in form initialization code
        for i in range (0, len(y)):
            xfl.fl_add_chart_value(fd_staticform.chart, y[i], label[i], \
                    i + 1)
        xfl.fl_add_nmenu_items(fd_choiceform.pulldown, \
                    "MenuEntry1|MenuEntry2|MenuEntry3|MenuEntry4")
        xfl.fl_add_nmenu_items(fd_choiceform.pushmenu, \
                     "MenuEntry1|MenuEntry2|MenuEntry3")
        xfl.fl_add_select_items(fd_choiceform.choice, \
                       "Choice1|Choice2|Choice3|Choice4|Choice5|Choice6")
        xfl.fl_load_browser(fd_choiceform.browser, "Readme")
        xfl.fl_addto_tabfolder(folder, "ButtonObj", fd_buttonform.buttonform)
        xfl.fl_addto_tabfolder(folder, "StaticObj", fd_staticform.staticform)
        xfl.fl_addto_tabfolder(folder, "ValuatorObj", \
                fd_valuatorform.valuatorform)
        xfl.fl_addto_tabfolder(folder, "ChoiceObj", fd_choiceform.choiceform)
        xfl.fl_addto_tabfolder(folder, "InputObj", fd_inputform.inputform)


if __name__ == '__main__':
    print("********* folder_new.py *********")
    Flfolder(len(sys.argv), sys.argv)
