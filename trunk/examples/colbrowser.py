#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  colbrowser.c XForms demo, with some adaptations.
#
#  colbrowser.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Test browser/slider and color handling. Select a colorname,
# the program will show the color. Change the sliders, the
# program will pick a colorname that has the closest color.
#

import os
import sys
#sys.path.append("..")
import xformslib as xfl


MAX_RGB = 3000

# the RGB data file does not have a standard location on unix.
rgbfile = "/usr/lib/X11/rgb.txt"
rgbfile_2 = "/usr/share/X11/rgb.txt"

#static RGBdb rgbdb[ MAX_RGB ];

class FlColbrowser(object):
    def __init__(self, lsysargv, sysargv):
        self.rgbdb = [{'r':0, 'g':0, 'b':0}] * MAX_RGB
        self.pcl = None
        self.pdbobj = None
        self.prescol = None
        self.pcolbr = None
        self.prs = None
        self.pgs = None
        self.pbs = None
        self.dbname = ""
        if os.path.exists(rgbfile):
            self.dbname = rgbfile
        elif os.path.exists(rgbfile_2):
            self.dbname = rgbfile_2
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form_cl()
        if self.load_browser(self.dbname):
            xfl.fl_set_object_label(self.pdbobj, self.dbname)
        else:
            xfl.fl_set_object_label(self.pdbobj, "None")
        xfl.fl_set_form_minsize(self.pcl, self.pcl.contents.w , \
                self.pcl.contents.h)
        xfl.fl_set_form_maxsize(self.pcl, 2 * self.pcl.contents.w , \
                2 * self.pcl.contents.h)
        xfl.fl_show_form(self.pcl, xfl.FL_PLACE_FREE, xfl.FL_TRANSIENT, \
                "RGB Browser")
        xfl.fl_do_forms()
        sys.exit(0)


    def set_entry(self, i):
        #RGBdb *db = rgbdb + i;
        #print("i", i, "rgbdb[i].r", self.rgbdb[i]['r'], "rgbdb[i].g",
        #        self.rgbdb[i]['g'], "rgbdb[i].b",  self.rgbdb[i]['b'])
        xfl.fl_freeze_form(self.pcl)
        xfl.fl_mapcolor(xfl.FL_FREE_COL4 + i, self.rgbdb[i]['r'], \
                self.rgbdb[i]['g'], self.rgbdb[i]['b'])
        xfl.fl_mapcolor(xfl.FL_FREE_COL4, self.rgbdb[i]['r'], \
                self.rgbdb[i]['g'], self.rgbdb[i]['b'])
        xfl.fl_set_slider_value(self.prs, self.rgbdb[i]['r'])
        xfl.fl_set_slider_value(self.pgs, self.rgbdb[i]['g'])
        xfl.fl_set_slider_value(self.pbs, self.rgbdb[i]['b'])
        #xfl.fl_redraw_object(self.prescol)
        xfl.fl_unfreeze_form(self.pcl)


    def br_cb(self, pobj, q):
        r = xfl.fl_get_browser(pobj)
        if r > 0:
            self.set_entry(r - 1)


    def read_entry(self, dataline):
        dataline1 = dataline.replace("\n", "")
        dataline2 = dataline1.replace("  ", " ")
        #dataline2 = dataline1.replace("   ", " ")
        #dataline3 = dataline2.replace("  ", " ")
        #print "dataline2", dataline2
        listline = dataline2.split()
        print(listline)
        r = listline[0]
        g = listline[1]
        b = listline[2]
        namel = listline[3:]
        name = " ".join(namel)
        return int(r), int(g), int(b), name


    def load_browser(self, fname):
        #RGBdb *db = rgbdb,
        ndb = 0
        contents = [0] * MAX_RGB
        #*dbs = db + MAX_RGB;
        lr = -1
        lg = -1
        lb = -1
        if not os.path.exists(fname):
            xfl.fl_show_alert("Load", fname, "Can't open database file", 0)
            return 0
        filep = open(fname, 'r')
        xfl.fl_freeze_form(self.pcl)
        # read the items
        #contents = filep.readlines()
        #filep.close()
        self.set_entry(0)
        #print("lencont", len(contents))
        #while ( db < dbs && read_entry( fp, &r, &g, &b, name ) )
        #for ndb in range(0, len(contents)):
        #while ndb < len(contents):
        while True:
            if ndb == 752:      #MAX_RGB:
                break
            #print "contents[ndb]", contents[ndb]
            #print "ndb", ndb
            contents[ndb] = filep.readline()
            print(contents[ndb])
            r, g, b, name = self.read_entry(contents[ndb])
            #print "#"+str(r)+"#"+str(g)+"#"+str(b)+"#"+name
            self.rgbdb[ndb]['r'] = r
            self.rgbdb[ndb]['g'] = g
            self.rgbdb[ndb]['b'] = b
            #print self.rgbdb[ndb]['r'], self.rgbdb[ndb]['g'], self.rgbdb[ndb]['b']
            # unique the entries on the fly
            if lr != r or lg != g or lb != b:
                lr = r
                lg = g
                lb = b
                buf = "(%3d %3d %3d) %s" % (r, g, b, name)          #sprintf( buf, "(%3d %3d %3d) %s", r, g, b, name)
                xfl.fl_addto_browser(self.pcolbr, buf)
            ndb += 1            # db++;
        filep.close()
        #if ndb < MAX_RGB:                         #db < dbs
        #    self.rgbdb[ndb]['r'] = 1000        #db->r = 1000;  /* sentinel
        #else:
        #    ndb -= 1                #db--;
        #    self.rgbdb[ndb]['r'] = 1000        #db->r = 1000;
        xfl.fl_set_browser_topline(self.pcolbr, 1)
        xfl.fl_select_browser_line(self.pcolbr, 1)
        self.set_entry(0)
        xfl.fl_unfreeze_form(self.pcl)
        #print self.rgbdb[5], self.rgbdb[4], self.rgbdb[10], self.rgbdb[100]
        return 1


    def search_entry(self, r, g, b):
        #RGBdb *db = rgbdb;
        ndb = 0
        mindiff = ~0
        j = 0
        #for ( i = j = 0; db->r < 256; db++, i++ )
        for i in range(0, MAX_RGB):
            if self.rgbdb[ndb]['r'] < 256:
                break
            diffr = r - self.rgbdb[ndb]['r']
            diffg = g - self.rgbdb[ndb]['g']
            diffb = b - self.rgbdb[ndb]['b']
            if True:         #ifdef xfl.FL_LINEAR
                diff = int(3.0 * xfl.FL_abs(r - self.rgbdb[ndb]['r']) + \
                        5.9 * xfl.FL_abs(g - self.rgbdb[ndb]['g']) + \
                        1.1 * xfl.FL_abs(b - self.rgbdb[ndb]['b']))
            else:
                diff = int(3.0 * (diffr * diffr) + \
                        5.9 * (diffg * diffg) + \
                        1.1 * (diffb * diffb))
            if mindiff > diff:
                mindiff = diff
                j = i
            ndb += 1
        return j


    def search_rgb(self, pobj, q):
        top = xfl.fl_get_browser_topline(self.pcolbr)
        r = int(xfl.fl_get_slider_value(self.prs))
        g = int(xfl.fl_get_slider_value(self.pgs))
        b = int(xfl.fl_get_slider_value(self.pbs))
        xfl.fl_freeze_form(self.pcl)
        xfl.fl_mapcolor(xfl.FL_FREE_COL4, r, g, b)
        #xfl.fl_redraw_object(self.prescol)
        i = self.search_entry(r, g, b)
        # change topline only if necessary
        if i < top or i > (top + 15):
            xfl.fl_set_browser_topline(self.pcolbr, i - 8)
        xfl.fl_select_browser_line(self.pcolbr, i + 1)
        xfl.fl_unfreeze_form(self.pcl)


    # change database
    def db_cb(self, pobj, q):
        p = xfl.fl_show_input("Enter new database name", self.dbname)
        if not p or p == self.dbname:
            return
        buf = p
        if self.load_browser(buf):
            self.dbname = buf
            xfl.fl_set_object_label(pobj, self.dbname)


    def done_cb(self, pobj, q):
        xfl.fl_finish()
        sys.exit(0)


    def create_form_cl(self):
        if self.pcl:
            return
        self.pcl = xfl.fl_bgn_form(xfl.FL_NO_BOX, 330, 385)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 330, 385, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_COL1)
        pobj = xfl.fl_add_box(xfl.FL_NO_BOX, 40, 10, 250, 30, "Color Browser")
        xfl.fl_set_object_lcol(pobj, xfl.FL_RED)
        xfl.fl_set_object_lsize(pobj, xfl.FL_HUGE_SIZE)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE + xfl.FL_SHADOW_STYLE)
        xfl.fl_set_object_gravity(pobj, xfl.FL_North, xfl.FL_North)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
        self.pdbobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 50, \
                250, 25, "")
        xfl.fl_set_object_boxtype(self.pdbobj, xfl.FL_BORDER_BOX)
        if xfl.fl_get_visual_depth() == 1:
            tmpcolr = xfl.FL_WHITE
        else:
            tmpcolr = xfl.FL_COL1
        xfl.fl_set_object_color(self.pdbobj, tmpcolr, xfl.FL_COL1)
        xfl.fl_set_object_callback(self.pdbobj, self.db_cb, 0)
        xfl.fl_set_object_gravity(self.pdbobj, xfl.FL_North, xfl.FL_North)
        xfl.fl_set_object_resize(self.pdbobj, xfl.FL_RESIZE_X)
        self.prescol = xfl.fl_add_box(xfl.FL_FLAT_BOX, 225, 90, 90, 35, "")
        xfl.fl_set_object_color(self.prescol, xfl.FL_FREE_COL4, \
                xfl.FL_FREE_COL4)
        xfl.fl_set_object_boxtype(self.prescol, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_resize(self.prescol, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(self.prescol, xfl.FL_NorthEast, \
                xfl.FL_East)
        self.prs = xfl.fl_add_valslider(xfl.FL_VERT_FILL_SLIDER, 225, 130, \
                30, 200, "")
        xfl.fl_set_object_color(self.prs, xfl.FL_COL1, xfl.FL_RED)
        xfl.fl_set_slider_bounds(self.prs, 0, 255)
        xfl.fl_set_slider_precision(self.prs, 0)
        xfl.fl_set_object_callback(self.prs, self.search_rgb, 0)
        #xfl.fl_set_object_return(self.prs, 0)
        xfl.fl_set_object_resize(self.prs, xfl.FL_RESIZE_Y)
        xfl.fl_set_object_gravity(self.prs, xfl.FL_NorthEast, \
                xfl.FL_SouthEast)
        xfl.fl_set_object_return(self.prs, xfl.FL_RETURN_CHANGED)
        self.pgs = xfl.fl_add_valslider(xfl.FL_VERT_FILL_SLIDER, 255, 130, \
                30, 200, "")
        xfl.fl_set_object_color(self.pgs, xfl.FL_COL1, xfl.FL_GREEN)
        xfl.fl_set_slider_bounds(self.pgs, 0, 255)
        xfl.fl_set_slider_precision(self.pgs, 0)
        xfl.fl_set_object_callback(self.pgs, self.search_rgb, 1)
        #xfl.fl_set_object_return(self.pgs, 0)
        xfl.fl_set_object_resize(self.pgs, xfl.FL_RESIZE_Y)
        xfl.fl_set_object_gravity(self.pgs, xfl.FL_NorthEast, \
                xfl.FL_SouthEast)
        xfl.fl_set_object_return(self.pgs, xfl.FL_RETURN_CHANGED)
        self.pbs = xfl.fl_add_valslider(xfl.FL_VERT_FILL_SLIDER, 285, 130, \
                30, 200, "")
        xfl.fl_set_object_color(self.pbs, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_slider_bounds(self.pbs, 0, 255)
        xfl.fl_set_slider_precision(self.pbs, 0)
        xfl.fl_set_object_callback(self.pbs, self.search_rgb, 2)
        #xfl.fl_set_object_return(self.pbs, 0)
        xfl.fl_set_object_resize(self.pbs, xfl.FL_RESIZE_Y)
        xfl.fl_set_object_gravity(self.pbs, xfl.FL_NorthEast, \
                xfl.FL_SouthEast)
        xfl.fl_set_object_return(self.pbs, xfl.FL_RETURN_CHANGED)
        self.pcolbr = xfl.fl_add_browser(xfl.FL_HOLD_BROWSER, 10, 90, \
                205, 240, "")
        xfl.fl_set_browser_fontstyle(self.pcolbr, xfl.FL_FIXED_STYLE)
        xfl.fl_set_object_callback(self.pcolbr, self.br_cb, 0)
        xfl.fl_set_object_gravity(self.pcolbr, xfl.FL_NorthWest, \
                xfl.FL_SouthEast)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 135, 345, \
                80, 30, "Done")
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)
        xfl.fl_set_object_gravity(pobj, xfl.FL_South, xfl.FL_South)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
        xfl.fl_end_form()
        xfl.fl_scale_form(self.pcl, 1.1, 1.0)


if __name__ == '__main__':
    print("********* colbrowser.py *********")
    FlColbrowser(len(sys.argv), sys.argv)
