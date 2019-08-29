#!/usr/bin/env python
# coding=utf-8


import os
import re
import time
import random
import requests


REQUEST = requests.session()
REQUEST_URL = 'https://www.douban.com/'
FORM_DATA = {'name': 'XXX',
             'password': 'XXX',
             'remember': 'XXX'}
COMMENT_URL = 'https://movie.douban.com/subject/26581837/comments?start=%s&limit=20&sort=new_score&status=P'


def login_douban():
    r = REQUEST.post(REQUEST_URL, data=FORM_DATA, timeout=60)
    if r.status_code not in [200]:
        raise RuntimeError('Login "%s" failed.' % REQUEST_URL)
    print ('Login douban successfully.')


def fetch_the_comments_for_one_page(n):
    r = REQUEST.get(COMMENT_URL % n, timeout=60)
    if r.status_code not in [200]:
        RuntimeError('Login "%s" failed.' % (COMMENT_URL % '0'))
    print ('Fetch the %sth page.' % str(n+1))
    comments = re.findall('<span class="short">(.*)</span>', r.text)
    with open('data/comments.txt', 'a+') as wp:
        wp.write('\n'.join(comments))


def scrapy_all_comments():
    if os.path.exists('data/comments.txt'):
        os.remove('data/comments.txt')

    for start in range(100):
        fetch_the_comments_for_one_page(start)
        time.sleep(random.random() * 3)


if __name__ == '__main__':
    login_douban()
    scrapy_all_comments()
