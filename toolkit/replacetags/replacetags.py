#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: dirkit
# Desc: deal with files and dirs
# author: leo.liu
# date: 2018.2.22

import os
import sys
import csv
import datetime
import getopt
from sys import argv
import argparse

import csvdictlist


def parsefile(filename, outfile, mapfile):
    dataDict = csvdictlist.readDictCSV(mapfile)
    #print dataDict

    f = file(filename)
    o = file(outfile, 'wb')

    str = f.read()

    for (k, v) in dataDict.items():
        str = str.replace(k, v)
        #print k, v

    # while True:
    #     line = f.readline()
    #     if len(line) == 0:
    #         break
    #
    #     for (k, v) in dataDict.items():
    #         line.replace(k, v)
    #
    #     print line

    o.write(str)

    f.close()
    o.close()



def main(args):

    rec_file = args.infile
    rec_o_file = args.outfile
    map_file = args.mapfile    #datetime.datetime.now().strftime('%Y-%m')

    if rec_o_file==None:
        rec_o_file = rec_file + "_o"
        print 'out file name is NOT given, use default: ', rec_o_file

    parsefile(rec_file, rec_o_file, map_file)

    print "-- done --" # " at: ", now

    # 读取记录文件，将累加，结果为{省,运营商, count}


if __name__ =="__main__":
	# main(sys.argv[1:])
    usage = ''' replace strs
    eg. replacetags.exe -f A.txt -m TextModify.csv -o outA.txt
    '''
    parser = argparse.ArgumentParser(usage=usage, description="help info")
    parser.add_argument("-f", "--infile", required=True, help="origin file")
    parser.add_argument("-o", "--outfile", help="out file, add '_o' at the end of filename default")
    parser.add_argument("-m", "--mapfile", required=True, help="the map file")
    # parser.add_argument("-p", "--plat", required=True, choices=['yx', 'cf', 'yjcf', 'yjqf'], help="平台[ 云信<yx>, 触发<cf>, 云集触发<yjcf>, 云集群发<yjqf> ]" )

    args=parser.parse_args()

    main(args)
