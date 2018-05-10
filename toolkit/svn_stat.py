#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_backup
# author: leo.liu
# date: 2018.5.10
  
'''
利用命令

svn co https://192.168.2.20/svn/DBToolKit/trunk

生成日志
svn log -v --xml D:\statsvn\trunk > D:\statsvn\trunk\svn.log

生成统计信息

java -jar statsvn.jar D:\statsvn\trunk\svn.log D:\statsvn\trunk

生成详细信息

java -jar statsvn.jar D:\statsvn\trunk\svn.log D:\statsvn\trunk -include **/*.java:**/*.jsp:**/*.js:**/*.css:**/*.xml -exclude **/js/jquery-1.6.2.min.js

等待一段时间，D:\statsvn目录下就会生成大量的统计文件，打开index.html即可进行查看。
'''

import os
import svn_notrunk
import svn_withtrunk
import svn_stat_index


def main():
    print 'stats projects with trunk ...'
    svn_withtrunk.statsvn()
    print 'stats projects without trunk ...'
    svn_notrunk.statsvn()
    print 'build index page...'
    svn_stat_index.buildindex()
    print 'done'

if __name__=="__main__":
    main()