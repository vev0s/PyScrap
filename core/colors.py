#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

import sys, colorama

if sys.platform == 'win32':
    colorama.init()
            
R = "\033[%s;31m"
B = "\033[%s;34m"
G = "\033[%s;32m"
W = "\033[%s;38m"
Y = "\033[%s;33m"
E = "\033[0m"