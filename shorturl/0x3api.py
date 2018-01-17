#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import json
import time
import datetime
import hashlib


getcodeurl = "https://0x3.me/apis/authorize/getCode"
gettokenurl = "https://0x3.me/apis/authorize/getAccessToken"
api_key = 'rPwMGHgKTi'
secret_key = "hSbWActHVdmdnhhGVfTPPZYpwOomYRMP"

def getsign(api_key, code, secret_key):
    #     SIGN签名算法：
    # 将需要签名的字段按照key进行从低到高排序（ksort）
    # 将排序过的参数按照key=value的格式依次连接，最后连接上secret_key
    # 对上一步得到的字符串进行MD5散列，将MD5值转为小写，该值即为sign
    request_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    signstr = "api_key=%scode=%srequest_time=%s%s"%(api_key, code, request_time, secret_key)
    #print "signstr: " + signstr
    m = hashlib.md5(signstr)
    return m.hexdigest()


def getCode():
    #url = "https://0x3.me/apis/authorize/getCode"
    req = urllib2.Request(getcodeurl)
    # print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    # print res
    # 返回数据的格式
    # {
    # "status": 1,
    # "info": "code request success",
    # "data": "OTY2MzYrY3ZQaWNSK1RIeHhnSGtPdW9MM3RITkdPUDhWVldURE50cVdlcGI0L3o3Q2t2UA=="
    # }
    data = json.loads(res)
    return data['data']

def getAccessToken():
    #url = "https://0x3.me/apis/authorize/getAccessToken"
    #api_key = "rPwMGHgKTi"
    print "apikey: " + api_key
    code = getCode()
    print "code: " + code
    request_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # time.time()
    print "time: " + request_time
    sign = getsign(api_key, code, secret_key)
    print "sign: " + sign
    # req = urllib2.Request(gettokenurl)
    #param =


def main():
    # request_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #print request_time
    getAccessToken()

#     {
#     "status": 1,
#     "info": "access token issue success",
#     "data": {
#         "access_token": "rPwMGHgKTi|1518585330|61b0fb9755fcc0fd036946a1552cbf5e",
#         "expire_time": "2018-02-14 13:15:30",
#         "expire_timestamp": 1518585330
#     }
#     }

if __name__=="__main__":
    main()
