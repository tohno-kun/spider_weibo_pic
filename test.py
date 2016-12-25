#!/usr/bin/python2
# -*- coding: utf-8 -*-

# import os
# s1 = r'C:\\test.txt'
# s = 'http:\/\/ww4.sinaimg.cn\/large\/c4e4b95agw1f7awf028qfj20yg2667ak.jpg'
# print os.path.basename(s)
# print os.path.split(s)[1]
# print os.path.splitdrive(s1)[0]
# print os.path.splitext(s)[1]
#
# basedir = 'E:\\'
# print os.path.join(basedir, os.path.basename(s))


# #coding:utf-8
# '''
# Created on 2012-6-25
# @author: lzs
# '''
#
# import random
# import socket
# import urllib2
# import cookielib
#
# ERROR = {
#     '0':'Can not open the url,checck you net',
#     '1':'Creat download dir error',
#     '2':'The image links is empty',
#     '3':'Download faild',
#     '4':'Build soup error,the html is empty',
#     '5':'Can not save the image to your disk',
# }
#
# class BrowserBase(object):
#
#     def __init__(self):
#         socket.setdefaulttimeout(20)
#
#     def speak(self,name,content):
#         print '[%s]%s' %(name,content)
#
#     def openurl(self,url):
#         """
#         打开网页
#         """
#         cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
#         self.opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
#         urllib2.install_opener(self.opener)
#         user_agents = [
#             'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#             'Opera/9.25 (Windows NT 5.1; U; en)',
#             'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#             'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#             'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#             'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#             "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#             "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
#
#         ]
#
#         agent = random.choice(user_agents)
#         self.opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
#         try:
#             res = self.opener.open(url)
#             print res.read()
#         except Exception,e:
#             self.speak(str(e)+url)
#             raise Exception
#         else:
#             return res
#
# if __name__=='__main__':
#     splider=BrowserBase()
#     splider.openurl('http://blog.csdn.net/v_JULY_v/archive/2010/11/27/6039896.aspx')

import requests
# login_url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
# base_url = "http://m.weibo.cn/page/json?containerid=1005053303323994_-_WEIBO_SECOND_PROFILE_WEIBO&page=1"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER',
         'Connection' : 'keep-alive'}
# s = requests.session()
# htmlj = s.get(base_url, headers = headers)
# print htmlj

#coding:utf-8
import json
from lxml import html


def etree_to_string(etree_name):
    etree_string = []
    for name in etree_name:
        if name.encode('utf-8').strip() != '':
            etree_string.append(name.encode('utf-8').strip())
    return etree_string

# with open("json.json") as jsonfile:
#     json_data = json.load(jsonfile)
jsonfile = requests.session().get('https://www.google.com', headers = headers)
print(jsonfile.text)
# json_data = json.load(jsonfile.text)
# print(type(json_data['items_html']))
# tree_base = html.fromstring(json_data['items_html'])
# xpath_base = r'//*[@class="js-tweet-text-container"]/p/text()'
# text = etree_to_string(tree_base.xpath(xpath_base))
# for i in text:
#     print(str(text.index(i)+1) +" : "+ i.decode("utf-8"))