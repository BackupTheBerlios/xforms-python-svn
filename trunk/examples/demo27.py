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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flslider import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *


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

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.init_colorpart()
        self.init_controlpart()
        self.init_mainpart()
        self.color_callback(self.pcolorobj, 0)

        while fl_do_forms():
            pass
        fl_finish()


    # color form callback routine
    def color_callback(self, pobj, d):
        self.r = int(255 * fl_get_slider_value(self.predsl))
        self.g = int(255 * fl_get_slider_value(self.pgreensl))
        self.b = int(255 * fl_get_slider_value(self.pbluesl))
        fl_mapcolor(FL_FREE_COL1, self.r, self.g, self.b)
        fl_redraw_object(self.pcolorobj)


    def create_colorform(self):
        if self.pcolorform:
            return

        self.pcolorform = fl_bgn_form(FL_NO_BOX, 315, 190)
        pobj = fl_add_box(FL_UP_BOX, 0, 0, 315, 190, "")
        self.pbluesl = fl_add_slider(FL_HOR_SLIDER, 20, 25, 220, 35, "")
        fl_set_object_color(self.pbluesl, FL_COL1, FL_BLUE)
        self.predsl = fl_add_slider(FL_HOR_SLIDER, 20, 135, 220, 35, "")
        fl_set_object_color(self.predsl, FL_COL1, FL_RED)
        self.pgreensl = fl_add_slider(FL_HOR_SLIDER, 20, 80, 220, 35, "")
        fl_set_object_color(self.pgreensl, FL_COL1, FL_GREEN)
        self.pcolorobj = fl_add_box(FL_BORDER_BOX, 250, 25, 50, 145, "")
        fl_set_object_color(self.pcolorobj, FL_FREE_COL1, FL_FREE_COL1)
        fl_end_form()


    # initializes the color part
    def init_colorpart(self):
        self.create_colorform()
        fl_set_form_callback(self.pcolorform, self.color_callback, 0)
        fl_set_form_position(self.pcolorform, 20, -300 - self.pcolorform.contents.h)
        fl_show_form(self.pcolorform, FL_PLACE_GEOMETRY, FL_TRANSIENT, \
                     "Color")
        fl_mapcolor(FL_FREE_COL1, self.r, self.g, self.b)
        fl_redraw_object(self.pcolorobj)


    def select_object(self, pobj, which):
        self.curobj = which


    # control form callback routine
    def control_callback(self, pobj, d):
        if fl_is_same_object(pobj, self.psizeobj):
            self.cursize = int(40 * fl_get_slider_value(self.psizeobj))
        elif fl_is_same_object(pobj, self.pexitobj):
            fl_finish()
            sys.exit(0)


    def create_controlform(self):
        self.pcontrolform = fl_bgn_form(FL_UP_BOX, 260, 230)

        fl_bgn_group()
        self.psquareobj = fl_add_button(FL_RADIO_BUTTON, 20, 150, 60, 60,
                                 "@square")
        fl_set_object_lcol(self.psquareobj, FL_YELLOW)
        fl_set_object_callback(self.psquareobj, self.select_object, 1)
        pobj = fl_add_button(FL_RADIO_BUTTON, 20, 90, 60, 60,
                            "@circle")
        fl_set_object_lcol(pobj, FL_YELLOW)
        fl_set_object_callback(pobj, self.select_object, 2)
        pobj = fl_add_button(FL_RADIO_BUTTON, 20, 30, 60, 60, 
                            "@8>")
        fl_set_object_lcol(pobj, FL_YELLOW)
        fl_set_object_callback(pobj, self.select_object, 3)
        fl_end_group()

        self.pexitobj = fl_add_button(FL_NORMAL_BUTTON, 160, 30, 80, 30, "Exit")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 160, 180, 80, 30, "Clear")
        fl_set_object_callback(pobj, self.clearit, 0)

        self.psizeobj = fl_add_slider(FL_VERT_SLIDER, 100, 30, 40, 180, "size")
        fl_set_slider_bounds(self.psizeobj, 0.025, 1.0)

        fl_end_form()


    # initializes the control part
    def init_controlpart(self):
        self.create_controlform()
        fl_set_form_callback(self.pcontrolform, self.control_callback, 0)
        fl_set_button(self.psquareobj, 1)
        fl_set_form_geometry(self.pcontrolform, 20, -self.pcontrolform.contents.h - 40,
                             self.pcontrolform.contents.w, self.pcontrolform.contents.h)
        fl_show_form(self.pcontrolform, FL_PLACE_SIZE, FL_TRANSIENT, \
                    "Control")


    def drawit(self, stobj):

        fl_winset(self.main_win)
        fl_mapcolor(FL_FREE_COL1, stobj.r, \
                    stobj.g, stobj.b)

        if stobj.type == 1:
            fl_rectf(stobj.x - stobj.size, \
                    stobj.y - stobj.size, 2 * stobj.size, \
                    2 * stobj.size, FL_FREE_COL1)
        elif stobj.type == 2:
            fl_circf(stobj.x, stobj.y, stobj.size, \
                    FL_FREE_COL1)
        elif stobj.type == 3:
            point = (FL_POINT * 3)()          # point[ 3 ]
            point[0].x = stobj.x - stobj.size
            point[0].y = stobj.y + stobj.size
            point[1].x = stobj.x + stobj.size
            point[1].y = stobj.y + stobj.size
            point[2].x = stobj.x
            point[2].y = stobj.y - stobj.size
            fl_polyf(point, 3, FL_FREE_COL1)


    # draws a particular object
    def drawobject(self):
        cur_obj = self.structob[self.onumb]                # OBJ *
        win_notused, x0, y0, km = fl_get_win_mouse(self.main_win)
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
        fl_redraw_form(self.pcontrolform)
        for i in range(0, self.onumb):
            self.drawit(self.structob + i)


    def clearit(self, pobj, data):
        self.onumb = 0
        fl_winbackground(self.main_win, fl_get_flcolor(FL_COL1))
        self.redrawit()


    # Event callback routine
    def main_callback(self, pxev, p):
        fl_winset(self.main_win)
        if pxev.contents.type == Expose:
            self.redrawit()
        elif pxev.contents.type == ButtonPress:
            self.drawobject()
        return 0


    def init_mainpart(self):
        fl_pref_wingeometry(400, 300, 400, 400)
        fl_pref_winsize(400, 400)
        fl_winbackground(0, fl_get_flcolor(FL_COL1))
        self.main_win = fl_winopen("Drawing")
        fl_set_event_callback(self.main_callback, 0)




if __name__ == '__main__':
    appl = Demo27(len(sys.argv), sys.argv)

