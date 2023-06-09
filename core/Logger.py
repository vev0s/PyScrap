#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

from core.colors import *

class Logger(object):
    """Note: this is an object class, you can call it by Logger().function(params)"""
    def success(self, str):
        print("%s[+] %s%s"%(G%0, str, E))

    def task(self, str):
        print("%s[~] %s%s"%(W%0, str, E))
    
    def error(self, str):
        print("%s[!] %s%s"%(R%0, str, E))

    def progress(self, str):
        print("%s[~] %s%s"%(Y%0, str, E), end='\r')