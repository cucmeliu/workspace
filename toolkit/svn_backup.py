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
import ftpkit
import dirkit

# 1. 逐个从存储项目名列表的文件中取出项目名
def exportPrjs(svn_base, svn_user, svn_pass, projects, export_dir):
    for project in projects:
        svn_url = svn_base + project
        target = export_dir + project
        # 2. export项目代码
        print 'Exporting %s'%(project)
        cmd = 'svn export %s %s  --username %s --password %s'%(svn_url, target, svn_user, svn_pass)
        if os.system(cmd) == 0:
            print 'Successful backup to ', target
        else:
            print 'Backup FAILED'
    print 'Done.'

def main():
    # def
    ##### test env
    # svn_base='https://127.0.0.1:8443/svn/'
    # svn_user='leo'
    # svn_pass='leo'
    # projects=['maven', 'svnTest', 'workspace']
    #
    # export_dir = 'c:\\temp\\rep\\export\\'
    #
    # zip_cmd='"C:\\Program Files\\7-Zip\\7z.exe" -p1323537 a -tzip'
    # zip_dir= 'c:\\temp\\rep\\zip\\'
    #
    # ftp_ip='192.168.1.248'
    # ftp_port='21'
    # ftp_dir='/incoming/leo/svn/'
    # ftp_user='winnerci'
    # ftp_pass='winnerci'
    ###########################

    ##### prod env
    svn_base='https://127.0.0.1:443/svn/'
    svn_user='ci'
    svn_pass='ciAdmin'
    projects=['35DbLocal', '41SmartCallCenter', '50winnerClean', '60Cloud', '60winnerMonitor', '61winnerCommon', 'docs', 'winnerMasServer', 'winnerSMS', 'winnerSMS-api', 'winnerSMS-sms', 'winnerVoiceNew', ]

    export_dir = 'F:\\backuprep\\export\\'

    zip_cmd='"C:\\7-Zip\\7z.exe" -p1323537 a -tzip'
    zip_dir= 'F:\\backuprep\\zip\\'

    ftp_ip='192.168.1.248'
    ftp_port='21'
    ftp_dir='/incoming/leo/svn/'
    ftp_user='winnerci'
    ftp_pass='winnerci'
    ###################################

    # exec
    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    print '------export------'
    exportPrjs(svn_base, svn_user, svn_pass, projects, export_dir)

    print '------zip------'
    zipfile = dirkit.zipBackups(zip_cmd, export_dir, zip_dir, 'ex'+ time.strftime('%Y%m%d%H%M%S') + '.7z')

    print '------Upload to ftp @ %s------'%(ftp_dir)
    ftp = ftpkit.ftpconnect(ftp_ip, ftp_port, ftp_user, ftp_pass)
    ftpkit.uploadfile(ftp, ftp_dir, zipfile)

    print '------rm exports------'
    dirkit.rmdir(export_dir)


    print '.Done.'


if __name__=="__main__":
    main()
