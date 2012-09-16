#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  iconvert.c XForms demo, with some adaptations.
#
#  iconvert.c was written by T.C. Zhao (03/1999).
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Convert an image file using the image support of Forms Library.
#
#  Usage: iconvert [-version][-verbose][-help] inputimage outimage [fmt]
#     output image format is determined by the extension or
#     by fmt if present.
#
#  Exit status:  0 (success) 1 (bad command line)  3 (conversion failed)
#

import sys
import os
#sys.path.append("..")
import xformslib as xfl


def main(lsysargv, sysargv):
    fmt = ""
    initialize()
    notoptargs = parse_command_line(lsysargv, sysargv)
    if len(notoptargs) == 4:        # $0, infile, outfile and fmt
        fmt = notoptargs[-1]
    elif len(notoptargs) == 3:      # $0, infile and outfile
        # get file extension without '.'
        fmt = (os.path.splitext(notoptargs[-1])[1]).replace(".", "")
    else:                           # too few or too much args
        usage(sysargv[0], 0)
    if not os.path.exists(notoptargs[0]):
        sys.exit(3)
    pimg = xfl.flimage_load(notoptargs[1])
    if xfl.flimage_dump(pimg, notoptargs[2], fmt) < 0:
        sys.exit(3)
    else:
        sys.exit(0)


def usage(strngcmd, more):
    msg = "Usage: %s [-verbose][-help] infile outfile [fmt]\n" % strngcmd
    print(msg)
    if not more:
        sys.exit(1)
    print("The output format is determined by the file extension " \
            "or fmt.\n fmt or extension must be one of the following\n")
    n = xfl.flimage_get_number_of_formats()
    k = 0
    msg = ""
    for i in range(1, n+1):
        pinfo = xfl.flimage_get_format_info(i)
        if pinfo.contents.read_write & xfl.FLIMAGE_WRITABLE:
            msg += "\t%s " % pinfo.contents.extension
            k += 1
            if k % 6 == 0:
                msg += "\n"
    print(msg)
    if k % 6:
        print("\n")
    sys.exit(1)


# shut up visual_cue
def noop(ptrimg, strng):
    return 0


def parse_command_line(lsysargv, sysargv):
    imgsetup.visual_cue = xfl.cfunc_int_ptrflimage_str(noop)
    argsnoopt = sysargv[:]
    for i in range(0, lsysargv):
        if sysargv[i].startswith("-"):
            if "-verb" in sysargv[i]:
                # setup.visual_cue = 0  TODO: find out how to pass 0 as func.
                imgsetup.visual_cue = xfl.cfunc_int_ptrflimage_str(noop)
                argsnoopt.remove(sysargv[i])
            elif "-h" in sysargv[i]:
                print("-h")
                usage(sysargv[0], 1)
            else:
                print("nunsesa")
                usage(sysargv[0], 0)
        else:
            continue
    xfl.flimage_setup(pimgsetup)
    return argsnoopt


def initialize():
    global imgsetup, pimgsetup
    imgsetup, pimgsetup = xfl.fls_make_flimagesetup_and_pointer()
    xfl.flimage_setup(pimgsetup)
    xfl.flimage_enable_xpm()
    xfl.flimage_enable_gif()
    xfl.flimage_enable_bmp()
    xfl.flimage_enable_sgi()
    xfl.flimage_enable_fits()
    xfl.flimage_enable_png()
    xfl.flimage_enable_xwd()
    xfl.flimage_enable_tiff()
    xfl.flimage_enable_ps()
    xfl.flimage_enable_jpeg()


if __name__ == '__main__':
    print("********* iconvert.py *********")
    main(len(sys.argv), sys.argv)
