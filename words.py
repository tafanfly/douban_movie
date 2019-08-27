#!/usr/bin/env python
# coding=utf-8


import os
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


CURDIR = os.path.abspath(os.path.dirname(__file__))
TEXT = os.path.join(CURDIR,  'data', 'comments.txt')
PICTURE= os.path.join(CURDIR,  'data', 'alice.png')
FONT = os.path.join(CURDIR, 'data', 'Songti.ttc')


def cut_the_words(test=TEXT):
    with open(test, 'r') as rp:
        content = rp.read()
    words_list = jieba.cut(content, cut_all = True)
    return ' '.join(words_list)


def create_worlds_cloud():
    background = np.array(Image.open(PICTURE))
    stopwords = set(STOPWORDS)
    for item in ["上海堡垒", "上海", "堡垒"]:
        stopwords.add(item)
    words = cut_the_words()
    wc = WordCloud(background_color="white",
                   mask=background,
                   stopwords=stopwords,
                   font_path=FONT)
    wc.generate(words)
    wc.to_file('data/girl.png')

if __name__ == '__main__':
    create_worlds_cloud()