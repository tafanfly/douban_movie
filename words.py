#!/usr/bin/env python
# coding=utf-8


import os
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


CURDIR = os.path.abspath(os.path.dirname(__file__))
PICTURE = os.path.join(CURDIR, 'data', 'girl.png')
COMMENTS = os.path.join(CURDIR, 'data', 'comments.txt')
FONT = os.path.join(CURDIR, 'data', 'Songti.ttc')
CLOUD = os.path.join(CURDIR, 'data', 'words.png')


def cut_the_words(path):
    with open(path, 'r') as rp:
        content = rp.read()
    words_list = jieba.cut(content, cut_all = True)
    return ' '.join(words_list)

def create_worlds_cloud(picture, data, font):
    background = np.array(Image.open(picture))
    words = cut_the_words(data)
    wc = WordCloud(background_color="white", mask=background, font_path=font)
    wc.generate(words)
    wc.to_file(CLOUD)

if __name__ == '__main__':
    create_worlds_cloud(picture=PICTURE, data=COMMENTS, font=FONT)

