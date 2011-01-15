#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo27.c XForms demo, with some adaptations.
#
#  demo27.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of event callbacks and form callbacks.
# purposesly mixed form callback, object callback and event callback
# to show the flexibility of Forms Library's event handling (and
# test if they actually work together).
#

import sys
#sys.path.append("..")
import xformslib as xfl


# Main part

class OBJ(object):
    type = 0
    r = 0
    g = 0
    b = 0
    x = 0
    y = 0
    size = 0


class Demo27(object):
    def __init__(self, lsysargv, sysargv):

        self.pcolorform = None    # placeholder
        # Color Part
        self.r = 128
        self.g = 128
        self.b = 128
        # Control Part
        self.curobj = 1
        self.cursize = 20

        self.structob = []
        for a in range(0, 10000):
            self.structob.append(OBJ())              # ob[ 10000 ]

        self.onumb = 0

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.init_colorpart()
        self.init_controlpart()
        self.init_mainpart()
        #self.color_callback(self.pcolorobj, 0)

        while xfl.fl_do_forms():
            pass
        xfl.fl_finish()


    # color form callback routine
    def color_callback(self, pobj, pvdata):
        ldata = xfl.convert_ptrvoid_to_ptrlongc(pvdata).contents.value
        print("ldata", ldata)

        self.r = int(255 * xfl.fl_get_slider_value(self.predsl))
        self.g = int(255 * xfl.fl_get_slider_value(self.pgreensl))
        self.b = int(255 * xfl.fl_get_slider_value(self.pbluesl))
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, self.r, self.g, self.b)
        xfl.fl_redraw_object(self.pcolorobj)


    def create_colorform(self):
        if self.pcolorform:
            return

        self.pcolorform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 315, 190)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 315, 190, "")
        self.pbluesl = xfl.fl_add_slider(xfl.FL_HOR_SLIDER, 20, 25, 220, 35, \
                "")
        xfl.fl_set_object_color(self.pbluesl, xfl.FL_COL1, xfl.FL_BLUE)
        self.predsl = xfl.fl_add_slider(xfl.FL_HOR_SLIDER, 20, 135, 220, 35, \
                "")
        xfl.fl_set_object_color(self.predsl, xfl.FL_COL1, xfl.FL_RED)
        self.pgreensl = xfl.fl_add_slider(xfl.FL_HOR_SLIDER, 20, 80, \
                220, 35, "")
        xfl.fl_set_object_color(self.pgreensl, xfl.FL_COL1, xfl.FL_GREEN)
        self.pcolorobj = xfl.fl_add_box(xfl.FL_BORDER_BOX, 250, 25, \
                50, 145, "")
        xfl.fl_set_object_color(self.pcolorobj, xfl.FL_FREE_COL1, \
                xfl.FL_FREE_COL1)
        xfl.fl_end_form()


    # initializes the color part
    def init_colorpart(self):
        self.create_colorform()
        xfl.fl_set_form_callback(self.pcolorform, self.color_callback, 0)
        xfl.fl_set_form_position(self.pcolorform, 20, \
                -300 - self.pcolorform.contents.h)
        xfl.fl_show_form(self.pcolorform, xfl.FL_PLACE_GEOMETRY, \
                xfl.FL_TRANSIENT, "Color")
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, self.r, self.g, self.b)
        xfl.fl_redraw_object(self.pcolorobj)


    def select_object(self, pobj, which):
        self.curobj = which


    # control form callback routine
    def control_callback(self, pobj, pvdata):
        ldata = xfl.convert_ptrvoid_to_ptrlongc(pvdata).contents.value
        print("ldata", ldata)
        if xfl.fl_is_same_object(pobj, self.psizeobj):
            self.cursize = int(40 * xfl.fl_get_slider_value(self.psizeobj))
        elif xfl.fl_is_same_object(pobj, self.pexitobj):
            xfl.fl_finish()
            sys.exit(0)


    def create_controlform(self):
        self.pcontrolform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 260, 230)

        xfl.fl_bgn_group()
        self.psquareobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 20, 150, \
                60, 60, "@square")
        xfl.fl_set_object_lcol(self.psquareobj, xfl.FL_YELLOW)
        xfl.fl_set_object_callback(self.psquareobj, self.select_object, 1)
        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 20, 90, 60, 60, \
                "@circle")
        xfl.fl_set_object_lcol(pobj, xfl.FL_YELLOW)
        xfl.fl_set_object_callback(pobj, self.select_object, 2)
        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 20, 30, 60, 60, 
                            "@8>")
        xfl.fl_set_object_lcol(pobj, xfl.FL_YELLOW)
        xfl.fl_set_object_callback(pobj, self.select_object, 3)
        xfl.fl_end_group()

        self.pexitobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 160, 30, \
                80, 30, "Exit")

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 160, 180, 80, 30, \
                "Clear")
        xfl.fl_set_object_callback(pobj, self.clearit, 0)

        self.psizeobj = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 100, 30, \
                40, 180, "size")
        xfl.fl_set_slider_bounds(self.psizeobj, 0.025, 1.0)

        xfl.fl_end_form()


    # initializes the control part
    def init_controlpart(self):
        self.create_controlform()
        xfl.fl_set_form_callback(self.pcontrolform, self.control_callback, 0)
        xfl.fl_set_button(self.psquareobj, 1)
        xfl.fl_set_form_geometry(self.pcontrolform, 20, \
                -self.pcontrolform.contents.h - 40, \
                self.pcontrolform.contents.w, self.pcontrolform.contents.h)
        xfl.fl_show_form(self.pcontrolform, xfl.FL_PLACE_SIZE, \
                xfl.FL_TRANSIENT, "Control")


    def drawit(self, stobj):

        xfl.fl_winset(self.main_win)
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, stobj.r, \
                    stobj.g, stobj.b)

        if stobj.type == 1:
            xfl.fl_rectf(stobj.x - stobj.size, \
                    stobj.y - stobj.size, 2 * stobj.size, \
                    2 * stobj.size, xfl.FL_FREE_COL1)
        elif stobj.type == 2:
            xfl.fl_circf(stobj.x, stobj.y, stobj.size, \
                    xfl.FL_FREE_COL1)
        elif stobj.type == 3:
            mylistpoint = [{'x':int(stobj.x - stobj.size), 'y':int(stobj.y + \
                    stobj.size)}, {'x':int(stobj.x + stobj.size), \
                    'y':int(stobj.y + stobj.size)}, {'x':int(stobj.x), \
                    'y':int(stobj.y - stobj.size)}]
            pxpoint = xfl.make_ptr_flpoint(mylistpoint)
            xfl.fl_polyf(pxpoint, 3, xfl.FL_FREE_COL1)


    # draws a particular object
    def drawobject(self):
        cur_obj = self.structob[self.onumb]                # OBJ *
        win_notused, x0, y0, km = xfl.fl_get_win_mouse(self.main_win)
        cur_obj.x = x0
        cur_obj.y = y0
        cur_obj.r = self.r
        cur_obj.g = self.g
        cur_obj.b = self.b
        cur_obj.type = self.curobj
        cur_obj.size = self.cursize
        self.drawit(cur_obj)
        self.onumb += self.onumb


    def redrawit(self):
        xfl.fl_redraw_form(self.pcontrolform)
        for i in range(0, self.onumb):
            self.drawit(self.structob + i)


    def clearit(self, pobj, data):
        self.onumb = 0
        xfl.fl_winbackground(self.main_win, xfl.fl_get_pixel(xfl.FL_COL1))
        self.redrawit()


    # Event callback routine
    def main_callback(self, pxev, pvdata):
        ldata = xfl.convert_ptrvoid_to_ptrlongc(pvdata).contents.value
        print("ldata", ldata)
        xfl.fl_winset(self.main_win)
        if pxev.contents.type == xfl.Expose:
            self.redrawit()
        elif pxev.contents.type == xfl.ButtonPress:
            self.drawobject()
        return 0


    def init_mainpart(self):
        xfl.fl_pref_wingeometry(400, 300, 400, 400)
        xfl.fl_pref_winsize(400, 400)
        xfl.fl_winbackground(0, xfl.fl_get_pixel(xfl.FL_COL1))
        self.main_win = xfl.fl_winopen("Drawing")
        xfl.fl_set_event_callback(self.main_callback, 0)



if __name__ == '__main__':
    print("********* demo27.py *********")
    Demo27(len(sys.argv), sys.argv)

