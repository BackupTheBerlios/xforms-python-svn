#!/bin/env python
# -*- coding: iso8859-1 -*-

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
__mainversion__ = "0.9.02a"                # real version
__vers_against_xforms__ = "1.0.94pre7"   # xforms version to be run against
__version__ = __mainversion__ + "_" + __vers_against_xforms__


#raise ImportError("This file is not meant to be imported directly.")

__all__ = ["flbasic", "flbitmap", "flbrowser", "flbutton", "flcanvas", \
          "flchart", "flclock", "flcounter", "flcursor", "fldial", \
          "flfilesys", "flflimage", "flformbrowser", "flglcanvas", \
          "flgoodies", "flinput", "flmisc", "flnmenu", "flpopup", \
          "flpositioner", "flscrollbar", "flselect", "flslider", \
          "flspinner", "fltabfolder", "flthumbwheel", "fltimer", \
          "flxbasic", "flxyplot", "xfdata", "library", "xfstruct"]

from .flbasic import *
from .flbitmap import *
from .flbrowser import *
from .flbutton import *
from .flcanvas import *
from .flchart import *
from .flclock import *
from .flcounter import *
from .flcursor import *
from .fldial import *
from .flfilesys import *
from .flflimage import *
from .flformbrowser import *
from .flglcanvas import *
from .flgoodies import *
from .flinput import *
from .flmisc import *
from .flnmenu import *
from .flpopup import *
from .flpositioner import *
from .flscrollbar import *
from .flselect import *
from .flslider import *
from .flspinner import *
from .fltabfolder import *
from .flthumbwheel import *
from .fltimer import *
from .flxbasic import *
from .flxyplot import *
from .xfdata import *
from .xfstruct import *



