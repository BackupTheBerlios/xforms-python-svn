#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  symbols.c XForms demo, with some adaptations.
#
#  symbols.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Show the built-in symbols
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


symbols = [ \
   "@>",      "@<-",     "@9->",     "@DnLine", "@8>",    "@circle",   "@->|",
   "@>>",     "@square", "@4->|",    "@8->|",   "@<->",   "@UpArrow",  "@9+",
   "@->",     "@<",      "@DnArrow", "@+",      "@-->",   "@line",     "@3->",
   "@UpLine", "@>|",     "@2-->",    "@4>|",    "@8>|",   "@=",        "@menu",
   "@8=",     "@|>",     "@2|>",     "@-32|>",  "@+32|>", "@-2circle", None]


#define N  ( sizeof symbols / sizeof * symbols - 1 )
N = len(symbols) / 2*len(symbols[0]) - 1


def done_cb(pobj, data):
    sys.exit(0)


def make_symbols():

    buf = ""
    x0 = y0 = 10
    dx = dy = 35
    ty = 17
    n = 7       #7
    xsep = 15+10
    ysep = 5+10

    w = (2 * x0 + n * dx + (n - 1) * xsep)
    tmpval = not (N % n)
    h = (2 * y0 + (1 + N / n - tmpval) * (dy + ty + ysep))

    pform = xf.fl_bgn_form(xfc.FL_FLAT_BOX, w+5, h+5)

    pobj0 = xf.fl_add_button(xfc.FL_HIDDEN_BUTTON, 0, 0, w, h, "")
    xf.fl_set_object_callback(pobj0, done_cb, 0)

    x = y = j = 0
    for i in range(0, len(symbols)):
        if not symbols[i]:
            break

        if (i % n == 0):
            x = x0
            y = y0 + j * (dy + ty + ysep + 1)
            j += 1
        else:
            x += dx + xsep

        pobj = xf.fl_add_box(xfc.FL_UP_BOX, x, y, dx, dy, symbols[i])
        xf.fl_set_object_lcol(pobj, xfc.FL_BOTTOM_BCOL)
        buf = " " + symbols[i]
        xf.fl_add_box(xfc.FL_FLAT_BOX, x, y + dy, dx, ty, buf)


    xf.fl_end_form()

    xf.fl_adjust_form_size(pform)

    return pform




def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    pform = make_symbols()
    xf.fl_show_form(pform, xfc.FL_PLACE_FREE, xfc.FL_FULLBORDER, "test")

    while xf.fl_do_forms():
        pass




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

