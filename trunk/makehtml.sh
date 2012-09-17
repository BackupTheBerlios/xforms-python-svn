#!/bin/sh
# Makes HTML API documentation

cd doc/html

PYTHONPATH=$PYTHONPATH:../../xformslib pydoc3 -w ../../xformslib/*.py
# hack to display common use modules and remove local path
sed -i "s|xformslib.||g" [xflv_]*.html
sed -i "s|<a href=\"file:/.*</a></font></td></tr></table>$| \
    <a href=\"index.html\">list</a></font></td></tr></table>|" [xflv_]*.html
# insert date of last modification
sed -i "s|</body>|<p>Updated on: $(date "+%Y-%m-%d %H:%M %z")</body>|" \
    [xflv_]*.html

cd ../..
