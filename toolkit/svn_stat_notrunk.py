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


##### prod env
svn_base='https://127.0.0.1:443/svn/'
# svn_user='ci'
# svn_pass='ciAdmin'
projects=[# '10winnerhome', 
# 'docs', 'incubator',
'yes云信', '高速触发管理平台']

# export_dir = 'F:\\backuprep\\export\\'

# zip_cmd='"C:\\7-Zip\\7z.exe" -p1323537 a -tzip'
# zip_dir= 'F:\\backuprep\\zip\\'

# 所有库的本地存放位置
repo_base   = 'F:\\backuprep\\svnlocal\\'
# 日志生成目录
log_dir     = 'F:\\backuprep\\logs\\' 
# 报告存放位置
rept_base   = 'F:\\backuprep\\reports\\' 
# 报告首页，项目列表
# idx_file    = 'F:\\backuprep\\reports\index.html'
# svnstat命令路径
stat_cmd    = 'F:\\backuprep\\statsvn-0.7.0\\statsvn.jar'  


# log_file='' #"$log_dir/svnstat.log"  
# log_day="$log_dir/2014-01-01_00:00:00"  
  
# version_start=4150  
# version_end=4159  

# def buildindex():
#     str = '<ul>'
#     for project in projects:
#         str = str + '<li><a href="%s" > %s </a></li>'%(project, project) 
#     str = str + '</ul>'

#     with open(idx_file, 'wb') as f:
#         f.write(str)

def statsvn():
    for project in projects:
        # project = project.decode('utf-8')
        svn_url = svn_base + project # + '/trunk/'
        # svn_url = svn_url.decode('utf-8')
        repo_trunk = repo_base + project # + '\\trunk\\'
        # repo_trunk = repo_trunk.decode('utf-8')
        log_file = log_dir + project + '.log'
        # log_file = log_file.decode('utf-8')
        rept_dir = rept_base + project
        # rept_dir = rept_dir.decode('utf-8')

        if not os.path.exists(repo_trunk):
            cmd = 'svn co %s %s'%(svn_url, repo_trunk)
        else:
            cmd = 'svn up %s '%(repo_trunk)
        # cmd = cmd.decode('utf-8')
        if os.system(cmd) == 0:
            print 'succ update ', project
        else:
            print 'FAILED update ', project

        cmd = 'svn log -v --xml %s > %s '%(repo_trunk, log_file)
        if os.system(cmd) == 0:
            print 'succ gen log for ', project
        else:
            print 'FAILED gen log for ', project

        cmd = 'java -jar %s %s %s -output-dir %s '%(stat_cmd, log_file, repo_trunk, rept_dir)
        if os.system(cmd) == 0:
            print 'succ gen stats for ', project
        else:
            print 'FAILED gen stats for ', project

def main():
    statsvn()

if __name__=="__main__":
    main()