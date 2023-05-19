#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

import argparse

def parser():
    argParser = argparse.ArgumentParser()
    
    argParser.add_argument("url", help="target URL")
    argParser.add_argument("-e", "--email", action="store_true", help="scrap e-mails")
    argParser.add_argument("-p", "--phone", action="store_true", help="scrap phone numbers")
    argParser.add_argument("-a", "--address", action="store_true", help="scrap address")
    argParser.add_argument("-l", "--log", action="store_true", help="show logs")

    return argParser.parse_args()