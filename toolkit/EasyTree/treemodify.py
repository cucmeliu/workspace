#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: treemodify
# Desc:  gene modify
# author: leo.liu
# date: 2018.2.28

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
        #print k, v
        ostr = ostr.replace(k, v)

    o.write(unicode(ostr).strip())
    f.close()
    o.close()


def main():
    (datasheet, row, col) = geneconcate.LoadDatasheet(DATASHEET)
    replacetree(datasheet, TREE_FILE)


if __name__ =="__main__":
    main()
