#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: treemodify
# Desc:  gene modify
# author: leo.liu
# date: 2018.2.28

import sys
import geneconcate


DATA_PATH = U'./data/'
DATASHEET = DATA_PATH + u'Datasheet.xlsx'
TREE_FILE = DATA_PATH + u'Tree.txt'

# 将基因树文件filename中形如(((((U019:0.18016606448247560000,(((U031:0.07106847917474014300,U029:0.07413699532635038800)
# 中U019, U031等，替换成Datasheet中Species和Strain No 的拼接串
def replacetree(datasheet, filename):
    data = datasheet[1:]
    dic = {}
    for row in data:
        uid = row[0]
        dic[row[0]] = row[1] + " " + row[2]

    f = file(filename)
    outfile = filename.replace('.txt', '_o.txt')
    o = file(outfile, 'wb')

    ostr = f.read()

    for (k, v) in dic.items():
        ostr = ostr.replace(k, v)

    #print ostr

    o.write(ostr)#(unicode(ostr).strip())
    f.close()
    o.close()


def do_main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    (datasheet, row, col) = geneconcate.LoadDatasheet(DATASHEET)
    replacetree(datasheet, TREE_FILE)
    return True

def main():
    do_main()

if __name__ =="__main__":
    main()
