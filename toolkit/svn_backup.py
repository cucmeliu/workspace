#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_backup
# author: leo.liu
# date: 2018.1.10
''' svn backup

backup svn projects
'''

import os
import time
from ftplib import FTP

# 1. 逐个从存储项目名列表的文件中取出项目名
def exportPrjs(svn_base, projects, export_dir):
    for project in projects:
        svn_url = svn_base + project
        target = export_dir + project
        # 2. export项目代码
        print 'Exporting %s'%(project)
        cmd = 'svn export %s %s'%(svn_url, target)
        if os.system(cmd) == 0:
            print 'Successful backup to ', target
        else:
            print 'Backup FAILED'
    print 'Done.'


# 3. 压缩
def zipBackups(zip_cmd, src_dir, dest_dir):
    # 7z a -tzip target_base + time.strftime('%Y%m%d%H%M%S') + '.7z'
    target = dest_dir + time.strftime('%Y%m%d%H%M%S') + '.7z'
    cmd = '%s %s %s'%(zip_cmd, target, src_dir)
    # print cmd
    if os.system(cmd) == 0:
        print 'Successful zip to ', target
    else:
        print 'zip FAILED'

    return target

# 4. 上传到ftp

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


def main():
    # def
    svn_base='https://127.0.0.1:8443/svn/'
    export_dir = 'c:\\temp\\rep\\export\\' #'F:/backuprep/export/'

    zip_cmd='"C:\\Program Files\\7-Zip\\7z.exe" -p1323537 a -tzip'
    zip_dir= 'c:\\temp\\rep\\zip\\' #'F:/backuprep/zip/'

    ftp_ip='192.168.1.248'
    ftp_port='21'
    ftp_dir='/incoming/leo/svn/'
    ftp_user='winnerci'
    ftp_pass='winnerci'

    projects=['maven', 'svnTest', 'workspace']
    # projects=['32SmsCloud', '35DbLocal', '36MMS', '37GlobalSMS']

    # exec
    print '------export------'
    exportPrjs(svn_base, projects, export_dir)

    print '------zip------'
    zipfile = zipBackups(zip_cmd, export_dir, zip_dir)

    print '------rm exports------'
    cmd = 'rd /s /q ' + export_dir
    print cmd
    if os.system(cmd) == 0:
        print 'Successful remove export dir '
    else:
        print 'rm export dir FAILED'

    print '------Upload to ftp @ %s------'%(ftp_dir)
    ftp = ftpconnect(ftp_ip, ftp_port, ftp_user, ftp_pass)
    uploadfile(ftp, ftp_dir, zipfile)
    print '.Done.'


if __name__=="__main__":
    main()
