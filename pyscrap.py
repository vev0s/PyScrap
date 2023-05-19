#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

import sys
# pyscrap.lib
from lib.parser import parser
from lib.output import *
from lib.banner import Banner
from lib.request import Request
from lib.colors import *
# pyscrap.scrap
from scrap.scrap import *
from scrap.email import *

class PyScrap:
    """PyScrap"""
    def __init__(self, url, **kwargs) -> None:
        """
        :param url: Target URL
        :param kwargs: See below

        :Keyword Arguments:colorama
            - **email**: TRUE/FALSE | Scrap e-mails
            - **phone**: TRUE/FALSE | Scrap phone numbers
            - **address**: TRUE/FALSE | Scrap address
            - **log**: TRUE/FALSE | Show logs
        :return:
        """
        self.url = url
        self.emails = kwargs.pop('email', True)
        self.phones = kwargs.pop('phone', False)
        self.address = kwargs.pop('address', False)
        self.log = kwargs.pop('log', False)

    def main(self):
        Banner().banner()

        scrap = Scrap(self.url)
        links = scrap.return_links()

        if self.emails:
            email = Email(links)
            output_emails(email._return_emails_list())
        if self.phones:
            pass
        if self.address:
            pass

if __name__ == '__main__':
    try:
        args = parser()
        PyScrap(args.url, email=args.email, phone=args.phone, address=args.address, logs=args.log).main()
    except KeyboardInterrupt as e:
        sys.exit("%sExiting.%s" % (R%0, E))