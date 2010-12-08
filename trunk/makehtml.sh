#!/bin/sh
# Makes HTML API documentation

cd doc/html
pydoc -w ../../xformslib/*.py
cd ../..
