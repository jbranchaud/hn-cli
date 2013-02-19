#!/usr/bin/python

import sys
import requests
from xml.dom import minidom
import urllib2

def main(argv):
    #request = requests.get('http://news.ycombinator.com/bigrss')
    f = urllib2.urlopen('http://news.ycombinator.com/bigrss')
    #xmldoc = minidom.parseString(request.text)
    xmldoc = minidom.parse(f)
    items = xmldoc.getElementsByTagName('item')
    for item in items:
        children = item.childNodes
        title = str(children[0].firstChild.nodeValue.encode('utf-8'))
        link = str(children[1].firstChild.nodeValue.encode('utf-8'))
        comments = str(children[2].firstChild.nodeValue.encode('utf-8'))
        print title + ' - ' + link + ' - ' + comments

if __name__ == "__main__":
    main(sys.argv[1:])
