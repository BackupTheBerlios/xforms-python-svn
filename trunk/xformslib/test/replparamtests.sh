#!/bin/sh
# Convenience script to replace ####PARAMS#### with a
# random sequence of params.

nameoffile=$1
newtext=$(python ./supplyrndparams.py)
sed "0,/####PARAMS####/s/####PARAMS####/$newtext/" $nameoffile > tmp$$$
mv tmp$$$ $nameoffile


