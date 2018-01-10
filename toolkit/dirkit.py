#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: dirkit
# Desc: deal with files and dirs
# author: leo.liu
# date: 2018.1.10

import os

def rmdir(dir):
    cmd = 'rd /s /q ' + dir
    #print cmd
    if os.system(cmd) == 0:
        print 'Successful remove dir',dir
    else:
        print 'FAIL to remove dir',dir


# 3. 压缩
    # zip_cmd='"C:\\Program Files\\7-Zip\\7z.exe" -p1323537 a -tzip'
    # zip_dir= 'C:\\workspace\\testCase\\'
def zipBackups(zip_cmd, src_dir, dest_dir, zipfilename):
    # 7z a -tzip target_base + time.strftime('%Y%m%d%H%M%S') + '.7z'
    target = dest_dir + zipfilename
    cmd = '%s %s %s'%(zip_cmd, target, src_dir)
    # print cmd
    if os.system(cmd) == 0:
        print 'Successful zip to ', target
    else:
        print 'zip FAILED'

    return target
