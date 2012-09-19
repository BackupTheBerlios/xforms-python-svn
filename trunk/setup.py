#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
from xformslib.__init__ import __version__
import glob, os

name = 'xforms-python'
version = __version__
long_description = """
xforms-python - Python wrapper for XForms X11 Window System GUI C toolkit.
"""
usrdocdir = os.path.join('share/doc', name+'-'+version)
usrdochtmldir = os.path.join('share/doc', name+'-'+version, 'html')
usrdatadir = os.path.join('share', name+'-'+version)
doc_files = ['./doc/ChangeLog', './doc/CREDITS', './doc/Docs.txt', './doc/INSTALL', \
        './doc/lgpl-2.1.txt', './doc/lgpl-3.0.txt', './doc/LICENSE', './doc/README', \
        './doc/TODO', './doc/USAGE']
html_files = glob.glob('./doc/html/*.html')
example_files = glob.glob("./examples/*.py")
example_files.extend(glob.glob("./examples/*.x[bp]m"))
example_files.extend(glob.glob("./examples/*.fd"))
example_files.append("./examples/Readme")
example_files.append("./examples/test.ps")
bin_files = './bin/fd2python.py'

setup(name = name,
    version = version,
    description = 'XForms python wrapper',
    long_description = long_description,
    author = 'Luca Lazzaroni (LukenShiro)',
    author_email = 'lukenshiro@ngi.it',
    license = 'LGPLv2.1+',
    platforms = 'POSIX',
    keywords = 'xforms python wrapper',
    url = 'http://xforms-python.berlios.de',
    packages = ['xformslib'],
    package_dir = {'xformslib' : 'xformslib'},
    scripts = [bin_files, ],
    data_files = [(usrdocdir, doc_files), \
            (usrdochtmldir, html_files), \
            (usrdatadir, example_files)]
    )
