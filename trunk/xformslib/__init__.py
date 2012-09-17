#!/bin/env python3
# -*- coding: utf-8 -*-

"""
    xforms-python - Python wrapper for XForms (X11) GUI C toolkit library
    using ctypes.

    Copyright (C) 2009-2012  Luca Lazzaroni "LukenShiro"
    e-mail: <lukenshiro@ngi.it>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, version 2.1 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU LGPL along with this
    program. If not, see <http://www.gnu.org/licenses/>.

    See CREDITS file to read acknowledgements and thanks to XForms,
    ctypes and other developers.
"""

# xforms-python version
__mainversion__ = "0.10.20120917"        # real version
__vers_against_xforms__ = "1.0.94pre12"  # xforms version to be run against
__version__ = __mainversion__ + "_" + __vers_against_xforms__


#raise ImportError("This file is not meant to be imported directly.")

__all__ = ["flbasic", "flbitmap", "flbrowser", "flbutton", "flcanvas", \
          "flchart", "flclock", "flcounter", "flcursor", "fldial", \
          "flfilesys", "flflimage", "flformbrowser", "flglcanvas", \
          "flgoodies", "flinput", "flmisc", "flnmenu", "flpopup", \
          "flpositioner", "flscrollbar", "flselect", "flslider", \
          "flspinner", "fltabfolder", "flthumbwheel", "fltimer", \
          "flxbasic", "flxyplot", "xfdata", "library", "xfstruct"]


from xformslib.flbasic import *
from xformslib.flbitmap import *
from xformslib.flbrowser import *
from xformslib.flbutton import *
from xformslib.flcanvas import *
from xformslib.flchart import *
from xformslib.flclock import *
from xformslib.flcounter import *
from xformslib.flcursor import *
from xformslib.fldial import *
from xformslib.flfilesys import *
from xformslib.flflimage import *
from xformslib.flformbrowser import *
from xformslib.flglcanvas import *
from xformslib.flgoodies import *
from xformslib.flinput import *
from xformslib.flmisc import *
from xformslib.flnmenu import *
from xformslib.flpopup import *
from xformslib.flpositioner import *
from xformslib.flscrollbar import *
from xformslib.flselect import *
from xformslib.flslider import *
from xformslib.flspinner import *
from xformslib.fltabfolder import *
from xformslib.flthumbwheel import *
from xformslib.fltimer import *
from xformslib.flxbasic import *
from xformslib.flxyplot import *
from xformslib.xfdata import *
from xformslib.xfstruct import *

