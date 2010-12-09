#!/bin/sh
# Makes HTML API documentation

cd doc/html

pydoc -w ../../xformslib/*.py
# hack to display common use modules and remove local path
sed -i "s|xformslib.||g" fl*.html
sed -i "s|<a href=\"file:/.*</a></font></td></tr></table>$| \
    <a href=\"index.html\">list</a></font></td></tr></table>|" [xflv]*.html

cd ../..
