#!/usr/bin/env python3
'''serialization and deserialization using XML instead of JSON'''

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """deserialize"""
    tree = ET.parse(filename)
    root = tree.getroot()
    deserialized_data = {}
    for child in root:
        deserialized_data[child.tag] = child.text
    return deserialized_data
