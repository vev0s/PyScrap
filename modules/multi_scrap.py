#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

# libs
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import threading
# pyscrap.modules
from modules.Email import *
from modules.Request import *
# pyscrap.core
from core.colors import *
from core.Logger import *

"""
email = Email(links)
output_emails(email._return_emails_list())
"""

class Scrap:
    def __init__(self, url) -> None:
        # self
        self.url = url
        self.links = []
        self.visited_urls = []

        # urlparse
        o = urlparse(self.url)
        self.netloc = o.netloc
        self.scheme = o.scheme

        # modules
        email = Email2()
        
        test("Looking for links...")
        self.get_all_pages(self.url)

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
        
    def return_links(self, content):
        try:
            links = []
            soup = BeautifulSoup(content, "html.parser")
            for i in soup.find_all('a'):
                href = i.get('href')
                o = urlparse(href)
                if "#js" in href:
                    continue
                if o.netloc == self.netloc:
                    links.append(href)
                elif o.netloc == '':
                    links.append("%s://%s%s" % (self.scheme, self.netloc, href))
            return links
        except Exception as e:
            exit(warn("%sERROR:%s %s (_return_page_links)" % (R%0, E, e)))
    
    def threaded_scrap(self, url):
        content = str(self._return_page_content(url))
        t1 = threading.Thread(target=return_links, args=(content,))
        t2 = threading.Thread(target=email, args=(content,))
        return

    def get_all_pages(self, url):
        Logger().task("Scrapping from %s" % url)
        content = str(self._return_page_content(url))
        links = self._return_page_links(content)
        for i in links:
            if i not in self.links:
                self.links.append(i)
                self.get_all_pages(i)

    def return_links(self):
        return self.links