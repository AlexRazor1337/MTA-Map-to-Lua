#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os, sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for element in sys.argv[1::]:
            if os.path.isfile(element):
                pass #TODO
            else:
                print("ERROR:", element, "is not a file!")
    else:
        sys.exit("ERROR: No file or directory specified!")