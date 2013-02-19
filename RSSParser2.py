#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
import urllib2

def main(argv):
    request = requests.get('http://news.ycombinator.com/rss')
    soup = BeautifulSoup(request.text)
    items = soup.find_all('items')
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        comments = item.find('comments').text
        print title + ' - ' + link + ' - ' + comments

if __name__ == "__main__":
    main(sys.argv[1:])
