#!/usr/bin/python2.7
#coding:utf-8

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'img src="(.*\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

html = getHtml("http://staymiao.lofter.com/?act=qbweekmagazine_20130609_01")
print getImg(html)