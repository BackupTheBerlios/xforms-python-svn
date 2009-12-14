#!/usr/bin/env python

import os, sys, getopt, shutil, glob
from xformslib.library import __version__

name = 'xforms-python'
version = __version__


exampleslist = glob.glob('examples/*')
defaultdatadir = '/usr/share/%s-%s' % (name, version)


def usage():
    print "This script installs xforms-python example files into datadir" \
	  " (default is: %s)\n" % defaultdatadir
    print "Usage:"
    print "python ./install-examples.py [--datadir=<your-data-directory>]\n"


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:", ["datadir="])
    except getopt.GetoptError:
	usage()
        sys.exit(2)
    datadir = defaultdatadir
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-d", "--datadir"):
            datadir = a
    try:
	if not os.path.exists(datadir):
	    os.mkdir(datadir)
    except OSError:
	print "Problem creating datadir %s." % datadir
    else:
	for example in exampleslist:
    	    if example.endswith('.py') or example.endswith('.xbm') or \
    	      example.endswith('.xpm'):
    		try:
    		    shutil.copy(example, datadir)
    		except OSError:
		    print "Problem copying examples in datadir: %s" % example



if __name__ == '__main__':
    main()

