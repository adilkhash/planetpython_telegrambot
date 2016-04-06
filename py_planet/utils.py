# -*- coding: utf8 -*-

from xml.etree import cElementTree

import requests


def parse_planetpy_rss():
    """Parses first 10 items from http://planetpython.org/rss20.xml
    """
    response = requests.get('http://planetpython.org/rss20.xml')
    parsed_xml = cElementTree.fromstring(response.content)
    items = []

    for node in parsed_xml.iter():
        if node.tag == 'item':
            item = {}
            for item_node in list(node):
                if item_node.tag == 'title':
                    item['title'] = item_node.text
                if item_node.tag == 'link':
                    item['link'] = item_node.text

            items.append(item)

    return items[:10]
