#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_hotcopy
# Desc: backup svn with hotcopy
# author: leo.liu
# date: 2018.1.10

import os
import time
import ftpkit
import dirkit



def main():
    ######### test env
    # rep_path='C:\\Repositories\\'
    # bak_path='C:\\workspace\\testCase\\svn\\'
    # projects=['svnTest', 'maven', 'workspace']
    #
    # zip_cmd='"C:\\Program Files\\7-Zip\\7z.exe" -p1323537 a -tzip'
    # zip_dir= 'C:\\workspace\\testCase\\'
    #
    # ftp_ip='192.168.1.248'
    # ftp_port='21'
    # ftp_dir='/incoming/leo/svn/'
    # ftp_user='winnerci'
    # ftp_pass='winnerci'
    ###############################

    ######## prod env
    rep_path='E:\\Repositories\\'
    bak_path='F:\\backuprep\\export\\'
    projects=['35DbLocal', '41SmartCallCenter', '50winnerClean', '60Cloud', '60winnerMonitor', '61winnerCommon', 'docs', 'winnerMasServer', 'winnerSMS', 'winnerSMS-api', 'winnerSMS-sms', 'winnerVoiceNew', ]

    zip_cmd= '"C:\\7-Zip\\7z.exe" -p1323537 a -tzip'
    zip_dir= 'F:\\backuprep\\zip\\'

    ftp_ip='192.168.1.248'
    ftp_port='21'
    ftp_dir='/incoming/leo/svn/'
    ftp_user='winnerci'
    ftp_pass='winnerci'
    #################################

    if not os.path.exists(bak_path):
        os.mkdir(bak_path)

    for prj in projects:
        cmd = 'svnadmin hotcopy %s %s '%(rep_path + prj, bak_path+prj)
        print cmd
        if os.system(cmd) == 0:
            print 'Successful hotcopy to ', rep_path
        else:
            print 'hotcopy FAILED'

    print '------zip------'
    zipfile = dirkit.zipBackups(zip_cmd, bak_path, zip_dir, 'hc'+ time.strftime('%Y%m%d%H%M%S') + '.7z')

    print '------Upload to ftp------'
    ftp = ftpkit.ftpconnect(ftp_ip, ftp_port, ftp_user, ftp_pass)
    ftpkit.uploadfile(ftp, ftp_dir, zipfile)

    print '------rm bak_path------'
    dirkit.rmdir(bak_path)

    print '.Done.'

if __name__=="__main__":
    main()
