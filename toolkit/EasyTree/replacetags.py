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

DATA_PATH = U'./data/'
RST_PATH = U'./data/result/'
IN_FILE = DATA_PATH + u'A.txt'
MAP_FILE = DATA_PATH + u'TextModify.csv'

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



def do_main(args):

    rec_file = IN_FILE if (args == None or args.infile == None) else args.infile
    rec_o_file = rec_file.replace('.txt', '_o.txt').replace(DATA_PATH, RST_PATH) if (args == None or args.outfile == None) else args.infile
    map_file = MAP_FILE if (args == None or args.mapfile == None) else args.mapfile

    parsefile(rec_file, rec_o_file, map_file)

    print "-- done --" # " at: ", now

    # 读取记录文件，将累加，结果为{省,运营商, count}
    return True

def main(args):
    if not os.path.exists(RST_PATH):
        os.mkdir(RST_PATH)
    do_main(args)


if __name__ =="__main__":
	# main(sys.argv[1:])
    usage = ''' replacetags [-f inputfile] [-o outputfile] [-m mapfile]
    eg. replacetags.exe -f A.txt -m TextModify.csv -o outA.txt
    '''
    parser = argparse.ArgumentParser(usage=usage, description="help info")
    parser.add_argument("-f", "--infile",  help="origin file")
    parser.add_argument("-o", "--outfile", help="out file, add '_o' at the end of filename default")
    parser.add_argument("-m", "--mapfile", help="the map file")
    # parser.add_argument("-p", "--plat", required=True, choices=['yx', 'cf', 'yjcf', 'yjqf'], help="平台[ 云信<yx>, 触发<cf>, 云集触发<yjcf>, 云集群发<yjqf> ]" )

    args=parser.parse_args()

    main(args)
