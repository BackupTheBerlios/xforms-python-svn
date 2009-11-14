import sys
import distutils.core


version = "0.1.0_1.0.92sp2"
long_description = """
xforms-python - Python wrapper for XForms X11 Windows System GUI C toolkit.
"""

distutils.core.setup(name = 'xforms-python',
                     version = version,
                     description = 'XForms python wrapper',
                     long_description = long_description,
                     author = 'Luca Lazzaroni (LukenShiro)',
                     author_email = 'lukenshiro@ngi.it',
                     license = 'LGPLv2.1',
                     platforms = 'POSIX',
                     keywords = 'xforms python wrapper',
                     url = 'http://xforms-python.berlios.de',
                     py_modules=['xformslib'],
                     data_files=[('share/doc/xforms-python-'+version, \
                                  ['doc/ChangeLog', \
                                  'doc/lgpl-2.1.txt', 'doc/INSTALL', \
                                  'doc/README', 'doc/TODO']), \
                                  ('share/xforms-python-'+version+'/examples', \
                                  ['examples/arrowbutton.py'])]
                     )

