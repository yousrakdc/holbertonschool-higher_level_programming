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
    result = {}
    for child in root:
        result[child.tag] = convert_value(child.text)
    return result


def convert_value(value):
    """convert the values"""
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value
