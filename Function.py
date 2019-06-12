# coding:  utf-8
# @Author: baobaozhou
import os
import shutil
import io

os.system('./TestImage.sh')
with io.open('./image_captioning/test/results.csv', 'r', encoding='utf-8')as f:
    for line in f.readlines():
        lineData = line.split(',')
        if lineData[1] != 'caption':
            with io.open('./text_style_transfer/data/yelp/sentiment.test.text', 'a',
                         encoding='utf-8')as t:
                t.write(lineData[1] + '\n')

os.system('./TestText.sh')
shutil.rmtree('checkpoints')
