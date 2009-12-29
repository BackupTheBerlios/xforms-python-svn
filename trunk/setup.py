#!/usr/bin/env python

from distutils.core import setup
import os, sys
from xformslib.library import __version__

name = 'xforms-python'
version = __version__
long_description = """
xforms-python - Python wrapper for XForms X11 Windows System GUI C toolkit.
"""

setup(name = name,
    version = version,
    description = 'XForms python wrapper',
    long_description = long_description,
    author = 'Luca Lazzaroni (LukenShiro)',
    author_email = 'lukenshiro@ngi.it',
    license = 'LGPLv2.1',
    platforms = 'POSIX',
    keywords = 'xforms python wrapper',
    url = 'http://xforms-python.berlios.de',
    packages=['xformslib'],
    package_dir={'xformslib' : 'xformslib'},
    data_files=[('doc/xforms-python-'+version, \
		 ['doc/ChangeLog', 'doc/CREDITS', 'doc/INSTALL', \
		 'doc/lgpl-2.1.txt', 'doc/LICENSE', 'doc/README', \
		 'doc/TODO'])]
    )

