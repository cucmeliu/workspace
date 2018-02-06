#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib, urllib2, sys
import ssl
import base64

def getToken():
	api_key = '9N4ScuNPHPUueWMO3FxdrTrO'
	secret_key = 'IhRG9hkCrO8ZpxRA1UGpWPxCozhlYglC'
	host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+api_key+'&client_secret=' +  secret_key
	request = urllib2.Request(host)
	request.add_header('Content-Type', 'application/json; charset=UTF-8')
	response = urllib2.urlopen(request)
	content = response.read()
	
	print content
	# {"access_token":"24.b9078a2dc2ab60bc670d1babcf965b90.2592000.1519294427.282335-10736267","session_key":"9mzdWWNj0d9vhY+kJBqRksHaDvNSFcSZr8WW5I\/MNez6jxZD7zYPW2EHbaUjOrM3YlL\/er7K\/\/je1\/gc2XIIcQy74MdnsA==","scope":"public vis-classify_dishes vis-classify_car brain_all_scope vis-classify_animal vis-classify_plant brain_object_detect brain_realtime_logo brain_dish_detect brain_car_detect brain_animal_classify brain_plant_classify wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower bnstest_fasf lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission","refresh_token":"25.dad0ce8df77d8ee8ca8b0e3355d514e1.315360000.1832062427.282335-10736267","session_secret":"a1df896868d0aa302de2e0e0d06cfb29","expires_in":2592000}

def object_detect(access_token, img_file):
	request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
	
	# 二进制方式打开图片文件
	f = open(img_file, 'rb')
	img = base64.b64encode(f.read())

	params = {"image":img,"with_face":1}
	params = urllib.urlencode(params)

	
	request_url = request_url + "?access_token=" + access_token
	request = urllib2.Request(url=request_url, data=params)
	request.add_header('Content-Type', 'application/x-www-form-urlencoded')
	response = urllib2.urlopen(request)
	content = response.read()
	if content:
		print content


def plant(access_token, img_file):
	'''
	植物识别
	'''

	request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

	# 二进制方式打开图片文件
	f = open(img_file, 'rb')
	img = base64.b64encode(f.read())

	params = {"image":img}
	params = urllib.urlencode(params)

	# access_token = '[调用鉴权接口获取的token]'
	request_url = request_url + "?access_token=" + access_token
	request = urllib2.Request(url=request_url, data=params)
	request.add_header('Content-Type', 'application/x-www-form-urlencoded')
	response = urllib2.urlopen(request)
	content = response.read()
	if content:
		print content.decode('utf-8')
		
def main():
	img_file='C:\\Users\\leo\\Downloads\\t019c5a8b26bf41f312.jpg'
	access_token = '24.b9078a2dc2ab60bc670d1babcf965b90.2592000.1519294427.282335-10736267'
	# object_detect(access_token, img_file)
	plant(access_token, img_file)

if __name__=="__main__":
    main()	
	