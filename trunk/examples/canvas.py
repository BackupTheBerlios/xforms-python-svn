#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  canvas.c XForms demo, with some adaptations.
#
#  canvas.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing the interaction with a canvas object.
#

import sys
#sys.path.append("..")
import xformslib as xfl


# Forms and Objects
class FD_canvasform(object):
    canvasform = None
    vdata = None
    cdata = ""
    ldata = 0
    canvas = None
    br = None
    keyboard = None
    mouse = None
    move = None
    misc = None

#static GC canvasGC;


class Flcanvas(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        #xfl.fl_color(xfl.FL_BLACK)

        self.fd_canvasform = self.create_form_canvasform()

        # fill-in form initialization code
        self.init_canvas(self.fd_canvasform)

        xfl.fl_show_form(self.fd_canvasform.canvasform, \
                xfl.FL_PLACE_FREE, xfl.FL_FULLBORDER, "My canvas form")

        xfl.fl_do_forms()
        xfl.fl_finish()


    def canvas_expose(self, pobj, win, w, h, pxev, pvdata):
        odata = xfl.convert_ptrvoid_to_ptrflobject(pvdata).contents
        print("odata:", odata)
        #FD_canvasform *ui = d;
        #XFillRectangle( fl_get_display( ), win, canvasGC, 0, 0, w, h );
        xfl.fl_rectangle(1, 0, 0, w, h, xfl.FL_YELLOW)
        xfl.fl_addto_browser(self.fd_canvasform.br, "Expose")
        return 0


    def canvas_key(self, pobj, win, w, h, pxev, pvdata):
        sdata = xfl.convert_ptrvoid_to_ptrstringc(pvdata).contents.value
        print("sdata:", sdata)
        #FD_canvasform *ui = d;
        #sprintf( buf, "KeyPress: keysym=%ld",
        #	 XKeycodeToKeysym( fl_display, ev->xkey.keycode, 0 ) );
        buf = "KeyPress: keysym=%ld" % pxev.contents.xkey.keycode
        xfl.fl_addto_browser(self.fd_canvasform.br, buf)
        return 0


    def canvas_but(self, pobj, win, w, h, pxev, pvdata):
        ddata = xfl.convert_ptrvoid_to_ptrfloatc(pvdata).contents.value
        print("ddata:", ddata)
        #FD_canvasform *ui = d;
        if pxev.contents.type == xfl.ButtonPress:
            tmpname = "Press"
        else:
            tmpname = "Release"
        #sprintf( buf, "Button%s: %d", ev->type == ButtonPress? "Press" : "Release",
        #		 ev->xbutton.button );
        buf = "Button%s: %d" % (tmpname, pxev.contents.xbutton.button)
        xfl.fl_addto_browser(self.fd_canvasform.br, buf)
        return 0


    def canvas_move(self, pobj, win, w, h, pxev, pvdata):
        fdata = xfl.convert_ptrvoid_to_ptrflform(pvdata).contents
        print("fdata:", fdata)
        #FD_canvasform *ui = d;
        #sprintf( buf, "Position: %d %d", ev->xmotion.x, ev->xmotion.y );
        buf = "Position: %d %d" % (pxev.contents.xmotion.x, \
                pxev.contents.xmotion.y)
        xfl.fl_addto_browser(self.fd_canvasform.br, buf)
        return 0


    def canvas_misc(self, pobj, win, w, h, pxev, pvdata):
        fdata = xfl.convert_ptrvoid_to_ptrflform(pvdata).contents
        print("fdata:", fdata)
        #FD_canvasform *ui = d;
        if pxev.contents.xcrossing.type == xfl.EnterNotify:
            tmpname = "Enter canvas"
        else:
            tmpname = "Leave canvas"
        xfl.fl_addto_browser(self.fd_canvasform.br, tmpname)
        return 0


    def init_canvas(self, fdui):
        xfl.fl_add_canvas_handler(fdui.canvas, xfl.Expose, \
                self.canvas_expose, fdui.canvas)
        xfl.fl_add_canvas_handler(fdui.canvas, xfl.KeyPress, \
                self.canvas_key, "mykey")
        xfl.fl_add_canvas_handler(fdui.canvas, xfl.ButtonPress, \
                self.canvas_but, 0.1)
        xfl.fl_add_canvas_handler(fdui.canvas, xfl.ButtonRelease, \
                self.canvas_but, 0.4)
        xfl.fl_set_button(fdui.mouse, 1)
        xfl.fl_set_button(fdui.keyboard, 1)
        #canvasGC = XCreateGC( fl_get_display( ),fl_state[ fl_vmode ].trailblazer,
        #					  0, 0 );
        #XSetForeground( fl_get_display( ), canvasGC, fl_get_flcolor( FL_BLACK ) );
        #xfl.fl_set_foreground(xfl.fl_root, xfl.fl_get_flcolor(xfl.FL_BLACK))


    # callbacks
    def sensitive_setting(self, pobj, evtnum):
        #FL_HANDLE_CANVAS hc;
        countn = 1
        events = [evtnum, 0]

        if evtnum == xfl.KeyPress:
            hc = self.canvas_key
        elif evtnum == xfl.ButtonPress:
            hc = self.canvas_but
            events[1] = xfl.ButtonRelease
            countn = 2
        elif evtnum == xfl.EnterNotify:
            hc = self.canvas_misc
            events[1] = xfl.LeaveNotify
            countn = 2
        elif evtnum == xfl.MotionNotify:
            hc = self.canvas_move
        else:
            return

        if xfl.fl_get_button(pobj):
            while countn > 0:
                countn -= 1
                xfl.fl_add_canvas_handler(self.fd_canvasform.canvas, \
                        events[countn], hc, self.fd_canvasform.canvasform)
        else:
            while countn > 0:
                countn -= 1
                xfl.fl_remove_canvas_handler(self.fd_canvasform.canvas, \
                        events[countn], hc)


    def disable_it(self, pobj, data):
        if xfl.fl_get_button(pobj):
            xfl.fl_deactivate_object(self.fd_canvasform.canvas)
        else:
            xfl.fl_activate_object(self.fd_canvasform.canvas)


    def hide_it(self, pobj, alln):
        if xfl.fl_object_is_visible(self.fd_canvasform.canvas):
            xfl.fl_hide_object(self.fd_canvasform.canvas)
            xfl.fl_set_object_label(pobj, "ShowCanvas")
        else:
            xfl.fl_show_object(self.fd_canvasform.canvas)
            xfl.fl_set_object_label(pobj, "HideCanvas")


    def clear_list(self, pobj, what):
        xfl.fl_clear_browser(self.fd_canvasform.br)


    def create_form_canvasform(self):
        fdui = FD_canvasform()

        fdui.canvasform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 450, 280)
        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 450, 280, "")

        fdui.canvas = xfl.fl_add_canvas(xfl.FL_NORMAL_CANVAS, 20, 40, \
                155, 187, "")
        xfl.fl_set_object_color(fdui.canvas, xfl.FL_BLACK, xfl.FL_COL1)

        fdui.br = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 188, 40, \
                152, 187, "")

        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 103, 10, 150, 20, \
                "Canvas Events")
        xfl.fl_set_object_lsize(pobj, xfl.FL_MEDIUM_SIZE)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)

        fdui.keyboard = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 345, 40, \
                76, 26, "Keyboard")
        xfl.fl_set_object_color(fdui.keyboard, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_object_callback(fdui.keyboard, self.sensitive_setting, \
                xfl.KeyPress)

        fdui.mouse = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 345, 70, 76, 26, \
                "Buttons")
        xfl.fl_set_object_color(fdui.mouse, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_object_callback(fdui.mouse, self.sensitive_setting, \
                xfl.ButtonPress)

        fdui.move = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 345, 100, 74, 26, \
                "Movements")
        xfl.fl_set_object_color(fdui.move, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_object_callback(fdui.move, self.sensitive_setting, \
                xfl.MotionNotify)

        fdui.misc = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 345, 130, \
                74, 26, "Enter\nLeave")
        xfl.fl_set_object_color(fdui.misc, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_object_callback(fdui.misc, self.sensitive_setting, \
                xfl.EnterNotify)

        pobj = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, 30, 240, 90, 27, "Deactivate")
        xfl.fl_set_object_callback(pobj, self.disable_it, 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 130, 240, 90, 27, \
                "Hide canvas")
        xfl.fl_set_object_callback(pobj, self.hide_it, 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 230, 240, 90, 27, "Clear")
        xfl.fl_set_object_callback(pobj, self.clear_list, 0)

        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 330, 240, 90, 27, "Done")

        xfl.fl_end_form()
        return fdui



if __name__ == '__main__':
    print("********* canvas.py *********")
    Flcanvas(len(sys.argv), sys.argv)

