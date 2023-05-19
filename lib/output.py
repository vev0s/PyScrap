#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

from lib.colors import *
from lib.banner import Banner

def plus(string):
    print("%s[+]%s %s"%(G%0, E, string))

def warn(string):
    print("%s[!] %s"%(R%0, string))

def test(string):
    print("%s[*] %s%s"%(B%0, string, E))

def info(string):
    print("%s[i]%s %s"%(Y%0, E, string))

def output_emails(emails):
    Banner().banner()
    for i in emails:
        plus(i)

def output_progress(str):
    pass