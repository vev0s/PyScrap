#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : PyScrap - Email & Phone Scrapper
# @url    : http://github.com/vev0s
# @author : Paul Lecomte (vev0s)

from setuptools import setup 

setup(
    name='PyScrap',

    version='0.0.1',
    description='Email & Phone Scrapper',
    url='https://github.com/vev0s',
    
    author = 'Paul (vev0s) Lecomte',
    author_email='vev0s.dev@gmail.com',
    license='MIT',

    install_requires = ['colorama','requests','bs4', 're', 'urllib.parse', 'argparse'],
    console =['pyscrap.py'],
)