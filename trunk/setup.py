#!/usr/bin/env python

from distutils.core import setup
import os, sys, shutil

name = 'xforms-python'
version = "0.1.0_1.0.92sp2"
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
    )
