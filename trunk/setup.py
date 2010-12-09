#!/usr/bin/env python

from distutils.core import setup
from xformslib.vers import __version__
import glob, os

name = 'xforms-python'
version = __version__
long_description = """
xforms-python - Python wrapper for XForms X11 Window System GUI C toolkit.
"""
doc_files = ['doc/ChangeLog', 'doc/CREDITS', 'doc/Docs.txt', 'doc/INSTALL', \
	    'doc/lgpl-2.1.txt', 'doc/LICENSE', 'doc/README', 'doc/TODO', 'doc/USAGE']
html_files = glob.glob('doc/html/*.html')
examples_files = glob.glob('examples/*.py') + glob.glob('examples/*.x?m')
examples_files.append('examples/Readme')


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
    data_files=[('doc/xforms-python-'+version, doc_files), \
		('doc/xforms-python-'+version+"/html", html_files), \
		('share/xforms-python-'+version, examples_files)]
    )
