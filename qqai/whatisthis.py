#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64
import random
import urllib
import urllib2
import hashlib
import json
import time
# from urllib import parse
# from urllib import request

from urllib import quote
from urllib import urlencode

# 签名算法
# 1. 计算步骤
# 用于计算签名的参数在不同接口之间会有差异，但算法过程固定如下4个步骤。
#
# 将<key, value>请求参数对按key进行字典升序排序，得到有序的参数对列表N
# 将列表N中的参数对按URL键值对的格式拼接成字符串，得到字符串T（如：key1=value1&key2=value2），URL键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8，而不是小写%e8
# 将应用密钥以app_key为键名，组成URL键值拼接到字符串T末尾，得到字符串S（如：key1=value1&key2=value2&app_key=密钥)
# 对字符串S进行MD5运算，将得到的MD5值所有字符转换成大写，得到接口请求签名
# 2. 注意事项
# 不同接口要求的参数对不一样，计算签名使用的参数对也不一样
# 参数名区分大小写，参数值为空不参与签名
# URL键值拼接过程value部分需要URL编码
# 签名有效期5分钟，需要请求接口时刻实时计算签名信息
# 更多注意事项，请查看常见问题

# // getReqSign ：根据 接口请求参数 和 应用密钥 计算 请求签名
# // 参数说明
# //   - $params：接口请求参数（特别注意：不同的接口，参数对一般不一样，请以具体接口要求为准）
# //   - $appkey：应用密钥
# // 返回数据
# //   - 签名结果
def getReqSign(params, appkey):
    # 1. 按Key字典升序排序
    # params = [(k,params[k]) for k in sorted(params.keys())]

    params = sorted(params.items(), key=lambda d:d[0])

    # print params

    # 2. 拼接URL键值对
    str = ''
    for (k, v) in params:
        # print(k, v)
        if v != '':
            str = str + k + '=' + urllib.quote(v) + '&'

    # 3. 拼接app_key
    str += 'app_key='+appkey

    # print str

    # 4. MD5运算+转换大写，得到请求签名
    sign = hashlib.md5(str.encode("utf-8")).hexdigest().upper()

    return sign


def doHttpPost(url, params):

    #py 2.6
    postdata = urlencode(params)
    #py 3
    #postdata = parse.urlencode(params).encode('utf-8')

    #print(postdata)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # py 2
    req = urllib2.Request(url, postdata)#json.dumps(postdata))
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    #res = json.loads(res_data.read())

    # py 3
    # req = request.Request(url, data=postdata, headers=headers)
    # data = urllib.request.urlopen(req).read()

    print res
    data = res.decode('utf-8')
    #print(data)

    # data = json.loads(data)
    # print(data['data'])


def main():
    #// 图片base64编码
    #path   = 'http://www.ikohoo.com/ikohoo/images/about_img_4.jpg'
    path = '/Users/apple/Downloads/101524095_2.png'

    with open(path, 'rb') as f:
        b64img = base64.b64encode(f.read())

    #// 设置请求数据
    appkey = '6MqCaZ2zVYh6wYxF'

    params = {
        'app_id': '1106586435',
        'image' : str(b64img),
        'nonce_str' : str(random.randint(10000, 99999)),
        'sign' : '',
        'time_stamp' : str(int(time.time())),
    }

    params['sign'] = getReqSign(params, appkey)

    print params

    # // 执行API调用
    url = 'https://api.ai.qq.com/fcgi-bin/image/image_tag'

    doHttpPost(url, params)


if __name__=="__main__":
    main()
