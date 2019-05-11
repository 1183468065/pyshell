# -*- coding: utf-8 -*-
import sys
import urllib

import requests

reload(sys)
sys.setdefaultencoding('utf8')


def getDatas(keyword, pages):
    params = []
    for i in range(30, 30 * pages + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1526377465547': ''
        })
    url = 'https://image.baidu.com/search/index'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i).json().get('data'))

    return urls


def getImg(datalist, path):
    x = 0
    for list in datalist:
        for i in list:
            if i.get('thumbURL') != None:
                print('正在下载：%s' % i.get('thumbURL'))
                urllib.urlretrieve(i.get('thumbURL'), path + '%d.jpg' % x)
                x += 1
            else:
                print('图片链接不存在')


if __name__ == '__main__':
    datalist = getDatas('高清电脑背景', 1)
    getImg(datalist, 'D:/baiduimage/')
