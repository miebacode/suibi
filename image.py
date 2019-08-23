# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:17:45 2019

@author: Administrator
"""
#import os
#import shutil
from PIL import Image
#import pytesseract
from wordcloud import WordCloud
import numpy as np
import jieba
'''currentpath = os.getcwd()
path='f:/tupian/'
list=os.listdir(path)
print(list)
for p in list:
    print(path+p)
    pa=path+p
    #Image=Image.open(pa)
    image=Image.open(pa)
    text=pytesseract.image_to_string(image,lang='chi_sim')
    print(text)
    print('=================================================')'''
# 分词
def trans_CN(text):
	# 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result
    
with open("C:/wordcloud.txt") as fp:
    text = fp.read()
    print(text)
    text = trans_CN(text)
    mask = np.array(Image.open("D:/xin2.png"))
    wordcloud = WordCloud(background_color="white",mask=mask,font_path = "C:\Windows\Fonts\STXINGKA.TTF").generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    

#print ("currentpath: ",currentpath)
#2. 返回指定目录下的所有文件和目录名:os.listdir()
#print:os.listdir():  ['test.txt', 'testRW.py', 'test1.txt', 'cmd.py', 'rwfile.py', 'downloadfile.py', 'date.py', 'time.py', 'datetime.py', 'file.py']
#print ("os.listdir(): ",os.listdir('f:/tupian'))

#Image = Image.open('D:/test.png')   # 打开图片
#text = pytesseract.image_to_string(Image,lang='chi_sim')  #使用简体中文解析图片
#print(text)

 