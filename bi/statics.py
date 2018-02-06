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
#import pandas as pd


def sortBase(filename):
    # df=pd.read_csv(rfilename,encoding='gb2312')
    # print df
    with open(filename,'rb') as csvfile:
        reader = csv.reader(csvfile)
        # rows= [row for row in reader]
        # print rows

        rst = ["","",""]
        for row in reader:
            rst.append([row[1], row[2], row[4]])
        return rst


def parsefile(filename, outfile):
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
            csvWriter.writerow([k,v])
        csvFile.close()

    # dataList = list(ab)
    # with open(outfile, 'wb') as csvFile:
    #     csvWriter = csv.writer(csvFile)
    #     for data in dataList:
    #         csvWriter.writerow(data)
    #     csvFile.close

def usage():
    print '''
        Usage
        statics -f filename
    '''

def main(argv):
    # params
    try:
        options, args = getopt.getopt(argv, "hf:",["help", "file="])
        print options
        if len(options[0]) < 2:
            usage()
            sys.exit()
    except getopt.GetoptError:
        sys.exit()

    rec_file = ''

    for option, value in options:
        if option in ("-h", "--help"):
            usage()
            sys.exit()

        if option in ("-f", "--file"):
            rec_file = value
        else: usage()


	# read and deal with base info
    # 读取最新号码段文件，按{号码段, 省, 运营商} 方式处理号码段，并按号码段排序
    #base_file = "C:\\workspace\\git\\workspace\\bi\\phonebase.csv"
    #rec_file = "C:\\workspace\\git\\workspace\\bi\\data\\201711.txt"
    rec_o_file = rec_file + "_o"
    #base = sortBase(base_file)

    # count by 号段，结果为 (1xxxxxx, count)
    now = datetime.datetime.now()
    now.strftime('%Y-%m-%d %H:%M:%S')
    print "begin------at: ", now

    parsefile(rec_file, rec_o_file)

    now = datetime.datetime.now()
    now.strftime('%Y-%m-%d %H:%M:%S')
    print "end------at: ", now



    # 读取记录文件，将累加，结果为{省,运营商, count}


if __name__ =="__main__":
	main(sys.argv[1:])
