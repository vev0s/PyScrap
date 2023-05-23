#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

from core.colors import *
from core.Banner import Banner

def plus(string):
    print("%s[+]%s %s"%(G%0, E, string))

def warn(string):
    print("%s[!] %s"%(R%0, string))

def test(string):
    print("%s[*] %s%s"%(B%0, string, E))

def info(string):
    print("%s[i]%s %s"%(Y%0, E, string))

def output_emails(emails, site):
    Banner().banner()
    f = open("wordlists/output.txt", "a")
    f.write("########## %s ##########")
    for i in emails:
        f.write("%s\n" % i)
        plus(i)
    f.close()
    print("---------------------------")
    info("Logged all emails into /wordlist/output.txt")

def output_progress(str):
    pass