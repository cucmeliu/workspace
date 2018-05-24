#!/usr/bin/python
# python 3
# -*- coding: UTF-8 -*-
# Filename: sendsms
# author: leo.liu
# date: 2018.5.22
import urllib

import pandas as pd
from urllib import parse, request


def send(phonelist):
    header_dict = {'Content-Type': 'application/json; charset=utf-8',
                   'Accept': '*/*',
                   'X-Requested-With': 'XMLHttpRequest',
                   #'Referer': 'https://www.newbenben.com/web/newbenben/regist.jsp?random=0.49269077203832484',
                   'Accept-Language': 'zh-CN',
                   'Accept-Encoding': 'gzip, deflate',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
                   #'Host': 'www.newbenben.com',
                   'Content-Length': '23',
                   'Connection': 'close',
                   'Cache-Control': 'no-cache',
                   'Cookie': 'JSESSIONID=ED241D160B0EE291BB7E2A22B48E71DD'
                   }
    url = 'https://www.newbenben.com/user/sendSmsCode2Register'

    for phone in phonelist:
        textmod = {"phone": '%s' %(phone) }
        # json串数据使用
        textmod = pd.io.json.dumps(textmod).encode(encoding='utf-8')
        print(textmod)

        req = request.Request(url=url, data=textmod, headers=header_dict)
        res = request.urlopen(req)
        res = res.read()
        print(res.decode(encoding='utf-8'))


def sendYuErWang(phonelist):
    header_dict = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Referer': 'http://user.ci123.com/account/NewAccount/?back_url=http://www.ci123.com/',
                   'Accept-Language': 'zh-CN',
                   'Accept-Encoding': 'gzip, deflate',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
                   'Content-Length': '25',
                   'Host': 'user.ci123.com',
                   'Pragma': 'no-cache',
                   'Cookie': 'UM_distinctid=1638687e9c0283-07f2164952f725-2a1d6c26-130980-1638687e9c13b5; PHPSESSID=a262c825503a96765110e6e58248e509; cck_lasttime=1527141456359; cck_count=0',
                   'Connection': 'close'
                   }
    url = 'http://user.ci123.com/api/Reg/sendauth'

    for phone in phonelist:
        textmod = {"mobile": '%s' %(phone), "type": "1"}

        textmod = parse.urlencode(textmod).encode(encoding='utf-8')
        print(textmod)

        req = request.Request(url=url, data=textmod, headers=header_dict)
        res = request.urlopen(req)
        res = res.read()
        print(res)
        print(res.decode(encoding='utf-8'))


def main():
  filename = 'phonelist.txt'
  phonelist = []

  for line in open(filename):
    phonelist.append(line.rstrip('\n'))

  print(phonelist)
  print('-----niu ben ben-----')
  send(phonelist)
  print('---- yu er wang ---')
  sendYuErWang(phonelist)


# post

if __name__ == "__main__":
    main()
