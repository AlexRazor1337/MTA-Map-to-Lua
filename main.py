#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os, sys
from lxml import etree

def generateCreateObjectString(object):
    final_string = ''
    
    modelid = object.xpath('@model')
    posX = object.xpath('@posX')
    posY = object.xpath('@posY')
    posZ = object.xpath('@posZ')
    
    rotX = object.xpath('@rotX')
    rotY = object.xpath('@rotY')
    rotZ = object.xpath('@rotZ')

    if rotX == '0' and rotY == '0' and rotZ == '0':
        final_string = "local object = createObject(%s, %s, %s, %s)" % (modelid, posX, posY, posZ)
    else:
        final_string = "local object = createObject(%s, %s, %s, %s, %s, %s, %s)" % (modelid, posX, posY, posZ, rotX, rotY, rotZ)

    interior = object.xpath('@interior')
    if interior != '0':
        final_string += "\nsetElementInterior(object, %s)" % (interior)

    dimension = object.xpath('@dimension')
    if dimension != '0':
        final_string += "\nsetElementDimension(object, %s)" % (dimension)

    collisions = object.xpath('@collisions')
    if collisions == 'false':
        final_string += "\nsetElementCollisionsEnabled(object, false)"

    alpha = object.xpath('@alpha')
    if alpha != '255':
        final_string += "\nsetElementAlpha(object, %s)" % (alpha)

    doublesided = object.xpath('@doublesided')
    if doublesided == 'true':
        final_string += "\nsetElementDoubleSided(object, true)"

    scale = object.xpath('@scale')
    if scale != '1':
        final_string += "\nsetElementScale(object, %s)" % (scale)

    return final_string


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