#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

from bs4 import BeautifulSoup
import re
from modules.Request import *
from core.Logger import *

class Email:
    def __init__(self, links) -> None:
        self.email_list = []
        self.links = links

        test("Looking for emails...")
        self._parse()

    def _parse(self):
        for i in self.links:
            #Logger().task("Looking for emails in %s" % i)
            content = Request(i).get_content()
            if content == "error":
                continue
            soup = BeautifulSoup(content, "html.parser")
            mails = self._find_emails(soup)
            for i in mails:
                if i not in self.email_list:
                    self.email_list.append(i)
        info("Found %s emails" % len(self.email_list))

    def _find_emails(self, soup):
        m = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', str(soup))
        return m
    
    def _return_emails_list(self):
        return self.email_list
