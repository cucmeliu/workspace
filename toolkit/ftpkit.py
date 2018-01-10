#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_hotcopy
# Desc: deal with ftp
# author: leo.liu
# date: 2018.1.10

import os
from ftplib import FTP

def ftpconnect(host, port, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    ftp.cwd(remotepath)

    bufsize = 1024
    fp = open(localpath, 'rb')
    file_name = os.path.split(localpath)[-1]
    ftp.storbinary('STOR ' + file_name, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
