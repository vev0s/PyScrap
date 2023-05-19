#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from modules.Email import *
from modules.Request import *
from core.colors import *
from core.Logger import *

class Scrap:
    def __init__(self, url) -> None:
        self.url = url
        self.links = []
        self.visited_urls = []

        o = urlparse(self.url)
        self.netloc = o.netloc
        self.scheme = o.scheme
        
        test("Searching for links...")
        self.get_all_pages(self.url)
        #Logger().task("Fetching pages from %s" % self.url)

    def _return_page_content(self, url):
        o = urlparse(url)
        if url not in self.visited_urls:
            try:
                content = Request(self.url).get_content()
                self.visited_urls.append(url)
                return content
            except Exception as e:
                exit(warn("%sERROR:%s %s (_return_page_content)" % (R%0, E, e)))
    
    def _return_page_links(self, content):
        try:
            links = []
            soup = BeautifulSoup(content, "html.parser")
            for i in soup.find_all('a'):
                href = i.get('href')
                o = urlparse(href)
                if o.netloc == self.netloc:
                    links.append(href)
                elif o.netloc == '':
                    links.append("%s://%s%s" % (self.scheme, self.netloc, href))
            return links
        except Exception as e:
            exit(warn("%sERROR:%s %s (_return_page_links)" % (R%0, E, e)))
    
    def get_all_pages(self, url):
        #Logger().task("Scrapping from %s" % url)
        content = str(self._return_page_content(url))
        links = self._return_page_links(content)
        for i in links:
            if i not in self.links:
                self.links.append(i)
                self.get_all_pages(i)

    def return_links(self):
        return self.links