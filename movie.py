#!/usr/bin/env python
# coding=utf-8


import os
import re
import time
import jieba
import random
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud


REQUEST = requests.session()
REQUEST_URL = 'https://www.douban.com/'
FORM_DATA = {'name': 'XXX',
             'password': 'XXX',
             'remember': 'false'}
COMMENT_URL = 'https://movie.douban.com/subject/26581837/comments?start=%s&limit=20&sort=new_score&status=P'


def login_douban():
    r = REQUEST.post(REQUEST_URL, data=FORM_DATA, timeout=60)
    if r.status_code not in [200]:
        raise RuntimeError('Login "%s" failed.' % REQUEST_URL)


def fetch_the_comments_for_one_page(n):
    r = REQUEST.get(COMMENT_URL % n, timeout=5)
    if r.status_code not in [200]:
        RuntimeError('Login "%s" failed.' % (COMMENT_URL % '0'))
    print ('Fetch the %sth page.' % n)
    comments = re.findall('<span class="short">(.*)</span>', r.text)
    with open('data.txt', 'a+') as wp:
        wp.write('\n'.join(comments))


def scrapy_all_comments():
    if os.path.exists('data.txt'):
        os.remove('data.txt')
    '''
    start = 0
    while fetch_the_comments_for_one_page(start):
        start += 1
    '''
    for start in range(50):
        fetch_the_comments_for_one_page(start)
        time.sleep(random.random() * 3)

def create_world_cloud():
    background_image = np.array(Image.open('456.jpg'))
    with open('data.txt') as rp:
        content = rp.read()
    words_list = jieba.cut(content, cut_all = True)
    words = ' '.join(words_list)
    my_wordcloud = WordCloud(background_color="white", mask=background_image, font_path="Songti.ttc")
    my_wordcloud.generate(words)
    plt.imshow(my_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    my_wordcloud.to_file("tiger.jpg")

if __name__ == '__main__':
    #login_douban()
    #fetch_the_comments_for_one_page()
    #scrapy_all_comments()
    create_world_cloud()

