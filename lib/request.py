#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

import requests
from lib.output import *
from lib.log import *

class Request:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_content(self):
        try:
            r = requests.get(self.url)
            return r.content
        except Exception as e:
            warn("%sFailed to establish a new connection with %s %s" % (R%0, self.url, E))
            return "error"