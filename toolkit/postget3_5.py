#!/usr/bin/python
# py3.5
# -*- coding: UTF-8 -*-
# Filename:
# author: leo.liu
# date: 2018.5.22

from urllib import parse, request
import json
from http import cookiejar

url = 'http://rapapi.org/mockjs/25632/v1/susers/suser'

def get():
    text = {'page': 1, 'per_page': 15, 'sortby': 'name', 'order': 'desc'}
    textmod = parse.urlencode(text)
    print(textmod)

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    req = request.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    print(res)
    print(res.decode(encoding='utf-8'))


def post():
    textmod = {'dob': '2018-05-23', 'nickname': 'leo', 'passwd': 'abc123', 'usercode': 'leoliu', 'username': 'leo.liu'}
    # json串数据使用
    textmod = json.dumps(textmod).encode(encoding='utf-8')
    # 普通数据使用
    textmod = parse.urlencode(textmod).encode(encoding='utf-8')
    print(textmod)

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}

    req = request.Request(url=url, data=textmod, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    print(res)
    print(res.decode(encoding='utf-8'))

def cookie():
    cj = http.cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj), request.HTTPHandler)
    request.install_opener(opener)
    # 下面进行正常请求


def main():
    get()
    post()

if __name__ == '__main__':
    main()