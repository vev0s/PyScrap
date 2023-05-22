#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

import sys, time
# pyscrap.core
from core.colors import *
from core.output import *
from core.Logger import *
from core.parser import parser
from core.Banner import Banner
# pyscrap.modules
from modules.Request import Request
from modules.Scrap import *
from modules.Email import *

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
        s_time = time.time()
        scrap = Scrap(self.url)
        links = scrap.return_links()

        if self.emails:
            info("Found %s pages \n---------------------------" % (len(links)))
            email = Email(links)
            output_emails(email._return_emails_list())
        if self.phones:
            pass
        if self.address:
            pass
        info("Scrapped URL in %s seconds" % (round(time.time() - s_time)))

if __name__ == '__main__':
    try:
        Banner().banner()
        args = parser()
        PyScrap(args.url, email=args.email, phone=args.phone, address=args.address, logs=args.log).main()
    except KeyboardInterrupt as e:
        sys.exit("%sExiting.%s" % (R%0, E))