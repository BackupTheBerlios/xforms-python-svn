#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" Provides some random parameters' values.
"""

import sys, os
import random
sys.path.append('..')

import xformslib as xfl

def provide_rnd_params():
    list1 = [0,1,2,3]
    list2 = [5,5]
    randlist = [1, 'Hello', 0, 15.0, 's', 254, xfl.FL_BLUE, None, 1001, \
            'E.U.', 4.5, 'Label', 15899, '88', xfl.KEY_list, 0.1, \
            'aabbccddee', list1, {'a':0, 'b':1}, 77.1234, None, \
            1.0, 'O', 154, list2, (0,0), 'iop', 'berries', 0x95]
    random.seed()
    nargs = random.randint(0, 8)        # max 8 args
    argstoret = ""
    if not nargs:
        return None
    else:       # some args
        for idx in range(0, nargs):
            posn = random.randint(0, len(randlist)-1)
            singarg = str(randlist[posn])
            argstoret = argstoret + singarg + ', '
        del list1, list2
        return argstoret

def main():
    listtosupply = provide_rnd_params()
    print(listtosupply)


if __name__ == '__main__':
    main()

