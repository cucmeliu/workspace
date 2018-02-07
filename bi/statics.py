#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: dirkit
# Desc: deal with files and dirs
# author: leo.liu
# date: 2018.2.6

import os
import sys
import csv
import datetime
import getopt
from sys import argv
import argparse
#import pandas as pd


# def sortBase(filename):
#     # df=pd.read_csv(rfilename,encoding='gb2312')
#     # print df
#     with open(filename,'rb') as csvfile:
#         reader = csv.reader(csvfile)
#         # rows= [row for row in reader]
#         # print rows
#
#         rst = ["","",""]
#         for row in reader:
#             rst.append([row[1], row[2], row[4]])
#         return rst

# class record:
#     def __init__(self):
#         self.phone = ''
#         self.count = 0
#         self.month = ''
#         self.plat = ''

def parsefile(filename, outfile, month, plat):
    f = file(filename)

    dataDict = {}
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        #print line,
        phone_pre = line[:7]

        if not dataDict.has_key(phone_pre):
            dataDict[phone_pre] = 1
        else:
            dataDict[phone_pre] = dataDict[phone_pre] + 1

    f.close()

    with open(outfile, "wb") as csvFile:
        csvWriter = csv.writer(csvFile)
        for k,v in dataDict.iteritems():
            csvWriter.writerow([k,v, month+'-1', plat])#'%d'%v+','+month])
        csvFile.close()

def main(args):

    rec_file = args.infile
    rec_o_file = args.outfile
    month = args.month    #datetime.datetime.now().strftime('%Y-%m')
    plat = args.plat

    if plat == 'yx':
        plat = '云信'
    elif plat == 'cf':
        plat = '触发'
    elif plat == 'yjcf':
        plat = '云集触发'
    elif plat == 'yjqf':
        plat = '云集群发'
    else:
        print '怎么会没填平台标识呢？'

    if rec_o_file==None:
        rec_o_file = rec_file + "_o"
        print '未指定输出文件名，默认使用: ', rec_o_file
    #base = sortBase(base_file)

    # count by 号段，结果为 (1xxxxxx, count)
    now = datetime.datetime.now()
    now.strftime('%Y-%m-%d %H:%M:%S')
    print "--parse begin at: ", now

    parsefile(rec_file, rec_o_file, month, plat)

    now = datetime.datetime.now()
    now.strftime('%Y-%m-%d %H:%M:%S')
    print "-- parse end at: ", now

    # 读取记录文件，将累加，结果为{省,运营商, count}


if __name__ =="__main__":
	# main(sys.argv[1:])
    parser = argparse.ArgumentParser(usage="号段统计工具", description="help info")
    parser.add_argument("-f", "--infile", required=True, help="要处理的文件")
    parser.add_argument("-o", "--outfile", help="输出文件名，如果未指定，则在infile后加_o")
    parser.add_argument("-m", "--month", required=True, help="YYYY-M, 导入内容的月份，如2018-1 ")
    parser.add_argument("-p", "--plat", required=True, choices=['yx', 'cf', 'yjcf', 'yjqf'], help="平台[ 云信<yx>, 触发<cf>, 云集触发<yjcf>, 云集群发<yjqf> ]" )

    args=parser.parse_args()

    main(args)
