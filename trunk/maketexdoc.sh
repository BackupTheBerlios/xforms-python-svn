#!/bin/sh

if [[ ! -x /usr/bin/epydoc ]]; then
    if [[ ! -x /usr/local/bin/epydoc ]]; then
        echo "You need epydoc to rebuild API documentation from python docstrings:\n"
        echo "It is not installed or not executable."
        exit 0
    fi
fi

epydoc -v --latex xformslib/library.py xformslib/xfdata.py -o doc/tex --url http://xforms-python.berlios.de

