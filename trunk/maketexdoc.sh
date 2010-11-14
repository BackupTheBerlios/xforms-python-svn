#!/bin/sh

if [[ ! -x /usr/bin/epydoc ]]; then
    if [[ ! -x /usr/local/bin/epydoc ]]; then
        echo "You need 'epydoc' to rebuild API documentation from python\n"
        echo "docstrings: it is not installed or not executable."
        exit 0
    fi
fi

# doc for xformslib/deprecated.py removed
epydoc -v -n xforms-python --docformat=restructuredtext --latex \
  xformslib/__init__.py xformslib/flbasic.py xformslib/flbitmap.py \
  xformslib/flbrowser.py xformslib/flbutton.py xformslib/flcanvas.py \
  xformslib/flchart.py xformslib/flclock.py xformslib/flcounter.py \
  xformslib/flcursor.py xformslib/fldial.py xformslib/flfilesys.py \
  xformslib/flflimage.py xformslib/flformbrowser.py xformslib/flglcanvas.py \
  xformslib/flgoodies.py xformslib/flinput.py xformslib/library.py \
  xformslib/flnmenu.py xformslib/flmisc.py xformslib/flpopup.py \
  xformslib/flpositioner.py xformslib/flscrollbar.py xformslib/flselect.py \
  xformslib/flslider.py xformslib/flspinner.py xformslib/fltabfolder.py \
  xformslib/flthumbwheel.py xformslib/fltimer.py xformslib/vers.py \
  xformslib/flxbasic.py xformslib/flxyplot.py xformslib/xfdata.py \
  xformslib/flstruct.py \
  -o doc/tex --url http://xforms-python.berlios.de
