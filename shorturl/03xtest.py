#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2

def post2(url, datas=None):
    req = urllib2.Request(url=url, data=urllib.urlencode(datas))
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res

def addurl(longurl):
    url = "https://0x3.me/apis/urls/add"
    params = {"longurl": longurl, "redirect_method": 302, "extra": "13812345678", "access_token": "rPwMGHgKTi|1518585330|61b0fb9755fcc0fd036946a1552cbf5e"}
    return post2(url=url, datas=params)

def main():
    shorturl = addurl("http://www.winnerlook.com/")
    print shorturl


if __name__=="__main__":
    main()
