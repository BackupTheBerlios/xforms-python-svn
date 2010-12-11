#!/usr/bin/env python

#  This file is part of xforms-python.
#
#  See LICENSE file for xforms-python license and copyright attribution.
#
# This demo shows a simple, resizable, not interactive table (not selectable,
# sortable or editable) for custom data.
#

import sys
#sys.path.append("..")
import xformslib as xfl



initx = inity = 0
wcell = 100     # standard width of a single cell
hcell = 25      # standard height of a single cell

coln_headers = ["Order", "Title", "Surname", "Name", "Sex", "Address", "Town"]
pbtncol = [c for c in range(0, len(coln_headers))]

table_values = ["10", "Mrs.", "Chen Yong", "Kayla", "F", \
        "300, Freemantle Plaza", "Armidale"], \
        ["3", "Mr.", "Smitherson", "William", "M", \
        "273, Whyalla Road", "Palmerstone"], \
        ["8", "Ms.", "Yamada", "Alyssa", "F", \
        "246, Rockdale Street", "Cairns"], \
        ["2", "Mr.", "Madison", "Lee", "M", \
        "219, Goulborn Avenue", "Murray Bridge"], \
        ["5", "Mrs.", "Rivera Delgado", "Emma", "F", \
        "192, Gladstone Heights", "Devonport"], \
        ["9", "Mr.", "Cohen", "Alex", "M", \
        "165, Bendigo Boulevard", "Benalla"], \
        ["4", "Ms.", "Knight", "Ella", "F", \
        "138, Hastings Lane", "Bayswater"], \
        ["7", "Mr.", "Fuchs", "John", "M", \
        "111, Nelson Alley", "Newcastle"], \
        ["1", "Mrs.", "Johanssen O'Riley", "Savannah", "F", \
        "84, Plymouth Square", "Shellharbour"], \
        ["6", "Mr.", "Bertrand", "Luke", \
        "M", "57, Auckland Drive", "Canterbury"], \
        ["11", "Ms.", "Hoffmann", "Ava", \
        "F", "30, Ebeye Place", "Hamilton"]

row_headers = [str(x) for x in range(1, len(table_values)+1)]
pbtnrow = [r for r in range(0, len(row_headers))]

#table_relpos = [(0,0), (100,0), (200,0), (300,0), (400,0), (500,0), (600,0)], \
#        [(0,25), (100,25), (200,25), (300,25), (400,25), (500,25), (600,25)], \
#        [(0,50), (100,50), (200,50), (300,50), (400,50), (500,50), (600,50)], \
#        [(0,75), (100,75), (200,75), (300,75), (400,75), (500,75), (600,75)], \
#        [(0,100), (100,100), (200,100), (300,100), (400,100), (500,100), (600,100)], \
#        [(0,125), (100,125), (200,125), (300,125), (400,125), (500,125), (600,125)], \
#        [(0,150), (100,150), (200,150), (300,150), (400,150), (500,150), (600,150)], \
#        [(0,175), (100,175), (200,175), (300,175), (400,175), (500,175), (600,175)], \
#        [(0,200), (100,200), (200,200), (300,200), (400,200), (500,200), (600,200)], \
#        [(0,225), (100,225), (200,225), (300,225), (400,225), (500,225), (600,225)], \
#        [(0,250), (100,250), (200,250), (300,250), (400,250), (500,250), (600,250)]

cellwidth = mincellwidth = []
for c in range(0, len(coln_headers)):
    cellwidth.append(0)
    mincellwidth.append(0)


class Flsimpletable(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "TableDemo", 0, 0)

        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, \
                (len(coln_headers)+1) * wcell, \
                (len(row_headers)+1) * hcell)

        pvertex = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, initx, inity, \
                wcell, hcell, "")
        xfl.fl_set_object_resize(pvertex, xfl.FL_RESIZE_ALL)
        self.set_column_headers()
        self.set_row_headers()
        self.fill_values_in_table()

        xfl.fl_end_form()

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_ASPECT, \
                xfl.FL_FULLBORDER, "SimpleTable")

        while xfl.fl_do_forms():
            pass                    # empty


    def fill_values_in_table(self):

        firstcellposx = initx + wcell
        firstcellposy = inity + hcell
        fontsize = xfl.FL_NORMAL_SIZE
        for row in range (0, len(row_headers)):
            for coln in range(0, len(coln_headers)):
                # set the size to fit text in
                cellvalue = table_values[row][coln]
                rightwidth = len(cellvalue)*10
                if rightwidth < wcell:          #mincellwidth[coln]
                    cellwidth[coln] = wcell     #mincellwidth[coln]
                    fontsize = xfl.FL_NORMAL_SIZE
                elif rightwidth >= wcell:       #mincellwidth[coln]
                    cellwidth[coln] = rightwidth
                    fontsize = xfl.FL_TINY_SIZE
                # fill cell with text
                ptxtcell = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, \
                             (wcell*coln) + firstcellposx, \
                             (hcell*row) + firstcellposy, \
                             cellwidth[coln], hcell, cellvalue)
                #ptxtcell = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, \
                #             table_relpos[row][coln][0] + firstcellposx, \
                #             table_relpos[row][coln][1] + firstcellposy, \
                #             cellwidth[coln], 25, table_values[row][coln])
                xfl.fl_set_object_lcol(ptxtcell, xfl.FL_GREENYELLOW)
                xfl.fl_set_object_lstyle(ptxtcell, xfl.FL_FIXED_STYLE)
                xfl.fl_set_object_lsize(ptxtcell, fontsize)
                xfl.fl_set_object_resize(ptxtcell, xfl.FL_RESIZE_ALL)
                if cellvalue.isdigit():
                    xfl.fl_set_object_lalign(ptxtcell, xfl.FL_ALIGN_RIGHT)
                else:
                    xfl.fl_set_object_lalign(ptxtcell, xfl.FL_ALIGN_LEFT)

        xfl.fl_adjust_form_size(self.pform)
        xfl.fl_redraw_form(self.pform)


    def set_column_headers(self):
        ch_dynx = initx
        ch_dyny = inity
        for coln in range(0, len(coln_headers)):
            ch_dynx += wcell
            pbtncol[coln] = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, ch_dynx, \
                                ch_dyny, wcell, hcell, coln_headers[coln])
            xfl.fl_set_object_lcol(pbtncol[coln], xfl.FL_YELLOW)
            xfl.fl_set_object_lstyle(pbtncol[coln], xfl.FL_BOLD_STYLE)
            xfl.fl_set_object_resize(pbtncol[coln], xfl.FL_RESIZE_ALL)
            xfl.fl_set_object_lalign(pbtncol[coln], xfl.FL_ALIGN_CENTER)


    def set_row_headers(self):
        rh_dynx = initx
        rh_dyny = inity
        for row in range(0, len(row_headers)):
            rh_dyny += hcell
            pbtnrow[row] = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, rh_dynx, \
                    rh_dyny, wcell, hcell, row_headers[row])
            xfl.fl_set_object_lcol(pbtnrow[row], xfl.FL_LAVENDER)
            xfl.fl_set_object_lstyle(pbtnrow[row], xfl.FL_BOLD_STYLE)
            xfl.fl_set_object_resize(pbtnrow[row], xfl.FL_RESIZE_ALL)



if __name__ == '__main__':
    print ("********* simpletable.py *********")
    Flsimpletable(len(sys.argv), sys.argv)

