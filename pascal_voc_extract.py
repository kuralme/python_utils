'''
Script to extract bounding boxes and frames to XML file
'''

import xml.etree.ElementTree as ET

def create_pascal_voc_xml(image, boxes, classes, folder_name, image_name):
    # Create a new XML file for the image
    root = ET.Element('annotation')
    folder = ET.SubElement(root, 'folder')
    folder.text = folder_name
    filename = ET.SubElement(root, 'filename')
    filename.text = image_name
    source = ET.SubElement(root, 'source')
    database = ET.SubElement(source, 'database')
    database.text = 'Unknown'
    size = ET.SubElement(root, 'size')
    width = ET.SubElement(size, 'width')
    width.text = str(image.shape[1])
    height = ET.SubElement(size, 'height')
    height.text = str(image.shape[0])
    depth = ET.SubElement(size, 'depth')
    depth.text = str(image.shape[2])

    # Loop over each bounding box and class label and add them to the XML file
    for bbox, cls in zip(boxes, classes):
        obj = ET.SubElement(root, 'object')
        name = ET.SubElement(obj, 'name')
        name.text = cls
        bndbox = ET.SubElement(obj, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        xmin.text = str(int(bbox[0]))
        ymin = ET.SubElement(bndbox, 'ymin')
        ymin.text = str(int(bbox[1]))
        xmax = ET.SubElement(bndbox, 'xmax')
        xmax.text = str(int(bbox[0] + bbox[2]))
        ymax = ET.SubElement(bndbox, 'ymax')
        ymax.text = str(int(bbox[1] + bbox[3]))

    # Save the XML file for the image as a string
    tree = ET.ElementTree(root)
    xml_string = ET.tostring(root, encoding='utf8', method='xml')
    return xml_string

