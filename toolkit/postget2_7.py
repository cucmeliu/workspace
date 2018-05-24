#!/usr/bin/python
# py2.7
# -*- coding: UTF-8 -*-
# Filename:
# author: leo.liu
# date: 2018.5.22
import json
import urllib, urllib2

url = 'http://rapapi.org/mockjs/25632/v1/susers/suser'

def get():
    text = {'page': 1, 'per_page': 15, 'sortby': 'name', 'order': 'desc'}
    textmod = urllib.urlencode(text)
    print(textmod)
    req = urllib2.Request(url='%s%s%s' %(url, '?', textmod))
    res = urllib2.urlopen(req)
    res = res.read()
    print(res)

def post():
    text = {'dob': '2018-05-23', 'nickname': 'leo', 'passwd': 'abc123', 'usercode': 'leoliu', 'username': 'leo.liu'}
    textmod = json.dumps(text)
    print textmod

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}

    req = urllib2.Request(url=url, data=textmod, headers=header_dict)
    res = urllib2.urlopen(req)
    res = res.read()
    print(res)


def main():
    get()
    # post()

if __name__ == '__main__':
    main()