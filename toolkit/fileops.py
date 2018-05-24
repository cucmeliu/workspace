#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: leo.liu
# date: 2018.5.22
# Filename: fileops
''' txtfile ops
'''


def readtxt1(filename):
	f = open(filename)
	line = f.readline()

	while line:
		print line,
		line = f.readline()

	f.close()

def readtxt2(filename):
	for line in open(filename):
		print line

def readtxt3(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		print line

	f.close()


def readexp():
	filename = 'array_reflection_2D_TM_vertical_normE_center.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
	pos = []
	Efield = []
	with open(filename, 'r') as file_to_read:
	  while True:
	    lines = file_to_read.readline() # 整行读取数据
	    if not lines:
	      break
	      pass
	     p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
	     pos.append(p_tmp)  # 添加新读取的数据
	     Efield.append(E_tmp)
	     pass
	   pos = np.array(pos) # 将数据从list类型转换为array类型。
	   Efield = np.array(Efield)
	   pass

def writetxt(filename):
	# 指定可写模式
	f1 = open(filename, 'w') # 清空原文件
	f2 = open(filename, 'r+') # 替换内容 
	f3 = open(filename, 'a') # 增加内容
	f1.write()


def otherops():
	f.readlines()
	f.next()
	f.writelines()

	f.seek(0|1|2)
	f.flush()
	f.tell()
	

def main():
	filename = 'C:\\workspace\\git\\workspace\\toolkit\\smsdealer\\phonelist.txt'
	readtxt1(filename)
	# readtxt2(filename)
	# readtxt3(filename)

	# writetxt(filename)




if __name__ == '__main__':
	main()
