#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os, sys
from lxml import etree

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for element in sys.argv[1::]:
            if os.path.isfile(element):
                with open(element) as file:
                    file_string = file.read().replace('edf:', '') # Parser doesn't like namespaces
                    root = etree.fromstring(file_string)
                    for obj in root.xpath("object"):
                        pass # TODO
            else:
                print("ERROR:", element, "is not a file!")
    else:
        sys.exit("ERROR: No file or directory specified!")