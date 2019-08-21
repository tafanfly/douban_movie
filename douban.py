#!/usr/bin/env python
# coding=utf-8


import requests


REQUEST_URL = 'https://www.douban.com/'
FORM_DATA = {'name': '15868857231',
             'password': 'nbsadmin3#',
             'remember': 'false'}


def login_douban():
    r = requests.post(REQUEST_URL, data=FORM_DATA, timeout=5)
    if r.status_code is 200:
        print 'Login "%s" successfully.' % REQUEST_URL
    else:
        print 'Login failed.'


if __name__ == '__main__':
    login_douban()
