#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os

import requests


'''微博爬虫
输入:json分析页地址
输出:下载图片到默认路径下'''

base_url = "http://m.weibo.cn/page/json?containerid=1005053303323994_-_WEIBO_SECOND_PROFILE_WEIBO"
basedir = r"E:\\onlyanose\\"

headers = {'Connection' : 'keep-alive'}
s = requests.session()
htmlj = s.get(base_url, headers=headers).json()
maxpage = htmlj['cards'][0]['maxPage']
L = []
for i in range(maxpage):
    url = "http://m.weibo.cn/page/json?containerid=1005053303323994_-_WEIBO_SECOND_PROFILE_WEIBO&page=%d" % i
    picj = s.get(url, headers=headers).json()
    for j in range(10):
        try:
            L.append(picj['cards'][0]['card_group'][j]['mblog']['original_pic'])
        except KeyError as e:
            pass

def long_time_task(name):
    print('Run task %s (%s)...') % (os.path.basename(name), os.getpid())
    with open(os.path.join(basedir, os.path.basename(name)),'wb') as f:
        try:
            f.write(s.get(name, headers=headers).content)
        except:
            print("%s download fail") % os.path.basename(name)
    print(r'Task %s is done.') % os.path.basename(name)

if __name__ == '__main__':
    print('Parent process %s.') % os.getpid()
    p = Pool(20)
    for pic in L:
        p.apply_async(long_time_task, args=(pic,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')