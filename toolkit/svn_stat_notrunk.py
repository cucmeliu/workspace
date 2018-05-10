#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_backup
# author: leo.liu
# date: 2018.5.10

import os
import logging
import svn_stat_func

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


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('svn_stat.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


def statsvn():
    for project in projects:
        project = project.decode('utf-8').encode('gbk')
        svn_url = svn_base + project # + '/trunk/'
        # svn_url = svn_url.decode('utf-8')
        repo_trunk = repo_base + project # + '\\trunk\\'
        # repo_trunk = repo_trunk.decode('utf-8')
        log_file = log_dir + project + '.log'
        # log_file = log_file.decode('utf-8')
        rept_dir = rept_base + project
        # rept_dir = rept_dir.decode('utf-8')

        logger.info('-- Deal with %s --'%(project))
        svn_stat_func.statsvn(project, svn_url, repo_trunk, log_file, rept_dir)

def main():
    statsvn()

if __name__=="__main__":
    main()