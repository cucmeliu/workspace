#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_backup
# author: leo.liu
# date: 2018.5.22
''' http kit
'''

#import requests
import urllib
import urllib2

def get2(url, datas=None):
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res

def post2(url, datas=None):
    req = urllib2.Request(url=url, data=urllib.urlencode(datas))
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res

def get(url, datas=None):
    response = requests.get(url, params=datas)
    json = response.json()
    return json

def post(url, datas=None):
     response = requests.post(url, data=datas)
     json = response.json()
     return json

def main():
    # 获取wordpress的文章分类信息
    #get_category_index = get2("http://35.202.208.84/wordpress/?json=get_category_index")
    #print get_category_index

    # 获取ID为XX的类下的所有文章
    #get_categories_posts = get2("http://35.202.208.84/wordpress/?json=get_categories_posts&categories_id=38")

    data = {"apikey":"apikey", "nonce_str":"nonce_str", "sign":"sign", "time":"1516004059","data":[{"ext":"1234", "mobile":"13812345678", "msg":"msgs", "uid":"0x12fa"}]}
    postmock = post2("http://192.168.1.171:8080/mockjsdata/1/sms/v2/sendsinglemsg", data)
    print postmock


if __name__=="__main__":
    main()
