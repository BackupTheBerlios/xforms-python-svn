#!/usr/bin/env python

import os, sys, getopt, shutil
from xformslib.library import __version__

name = 'xforms-python'
version = __version__


exampleslist = ['examples/arrowbutton.py', 'examples/bm1.xbm', \
	'examples/bm2.xbm', 'examples/borderwidth.py', \
	'examples/browserop.py', 'examples/buttonall.py', \
	'examples/choice.py', 'examples/colsel1.py', \
	'examples/colsel.py', 'examples/crab45.xpm', \
	'examples/crab.xpm', 'examples/cursor.py', \
	'examples/demo05.py', 'examples/demo06.py', \
	'examples/demo33.py', 'examples/fdial.py', \
	'examples/flclock.py', 'examples/fonts.py', \
	'examples/free1.py', 'examples/goodies.py', \
	'examples/invslider.py', 'examples/lalign.py', \
	'examples/ldial.py', 'examples/longlabel.py', \
	'examples/ndial.py', 'examples/objinactive.py', \
	'examples/objpos.py', 'examples/porsche.xpm', \
	'examples/positioner.py', 'examples/positionerXOR.py', \
	'examples/preemptive.py', 'examples/pushbutton.py', \
	'examples/pushme.py', 'examples/rescale.py', \
	'examples/secretinput.py', 'examples/sld_alt.py', \
	'examples/sldinactive.py', 'examples/sld_radio.py', \
	'examples/sldsize.py', 'examples/sliderall.py', \
	'examples/srs.xbm', 'examples/strsize.py', \
	'examples/symbols.py', 'examples/thumbwheel.py', \
	'examples/timerprec.py', 'examples/timer.py', \
	'examples/touchbutton.py', 'examples/yesno_cb.py', \
	'examples/yesno.py']

defaultdatadir = '/usr/share/%s-%s' % (name, version)


def usage():
    print "This script installs xforms-python example files into datadir" \
	  " (default is:%s)\n" % defaultdatadir
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
        os.mkdir(datadir)
    except OSError:
	print "Problem creating datadir."
    else:
	try:
	    for example in exampleslist:
		shutil.copy(example, datadir)
	except OSError:
	    print "Problem copying examples in datadir."



if __name__ == '__main__':
    main()

