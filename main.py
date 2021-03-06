#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os, sys
from lxml import etree

def generateCreateObjectString(object):
    final_string = ''
    
    modelid = object.xpath('@model')[0]
    posX = object.xpath('@posX')[0]
    posY = object.xpath('@posY')[0]
    posZ = object.xpath('@posZ')[0]
    
    rotX = object.xpath('@rotX')[0]
    rotY = object.xpath('@rotY')[0]
    rotZ = object.xpath('@rotZ')[0]

    if rotX == '0' and rotY == '0' and rotZ == '0':
        final_string = "object = createObject(%s, %s, %s, %s)" % (modelid, posX, posY, posZ)
    else:
        final_string = "object = createObject(%s, %s, %s, %s, %s, %s, %s)" % (modelid, posX, posY, posZ, rotX, rotY, rotZ)

    interior = object.xpath('@interior')[0]
    if interior != '0':
        final_string += "\nsetElementInterior(object, %s)" % (interior)

    dimension = object.xpath('@dimension')[0]
    if dimension != '0':
        final_string += "\nsetElementDimension(object, %s)" % (dimension)

    collisions = object.xpath('@collisions')[0]
    if collisions == 'false':
        final_string += "\nsetElementCollisionsEnabled(object, false)"

    alpha = object.xpath('@alpha')[0]
    if alpha != '255':
        final_string += "\nsetElementAlpha(object, %s)" % (alpha)

    doublesided = object.xpath('@doublesided')[0]
    if doublesided == 'true':
        final_string += "\nsetElementDoubleSided(object, true)"

    scale = object.xpath('@scale')[0]
    if scale != '1':
        final_string += "\nsetElementScale(object, %s)" % (scale)

    return final_string + '\n'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for element in sys.argv[1::]:
            if os.path.isfile(element):
                try:
                    with open(element) as file:
                        file_string = file.read().replace('edf:', '') # Parser doesn't like namespaces
                        root = etree.fromstring(file_string)
                        if root.xpath("count(object)") > 0:
                            output_file_name = os.path.abspath(element).rsplit(os.sep, 1)[0] + os.sep + os.path.basename(element).rsplit('.', 1)[0] + '.lua'
                            output_file = open(output_file_name, 'w+')

                            output_file.write("local object\n")

                            for obj in root.xpath("object"):
                                output_file.write(generateCreateObjectString(obj))

                            output_file.close()

                except etree.XMLSyntaxError:
                    print("ERROR:", element, "is not a valid xml file!")
            else:
                print("ERROR:", element, "is not a file!")
    else:
        sys.exit("ERROR: No file or directory specified!")