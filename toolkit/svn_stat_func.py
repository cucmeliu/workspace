#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_backup
# author: leo.liu
# date: 2018.5.10
  

import os
import logging

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


def statsvn(project, svn_url, repo_trunk, log_file, rept_dir):

    logger.info('svn: '+ svn_url)
    logger.info('rep: '+ repo_trunk)
    logger.info('log: '+ log_file)
    logger.info('rpt: '+ rept_dir)

    logger.info('----------update project code ..................')
    if not os.path.exists(repo_trunk):
        cmd = 'svn co %s %s'%(svn_url, repo_trunk)
    else:
        cmd = 'svn up %s '%(repo_trunk)

    # if os.system(cmd) == 0:
    #     logger.info('succ update ', project)
    # else:
    #     logger.warning('FAILED update ', project)
    logger.info(os.popen(cmd))

    logger.info('----------generate log  ..................')
    cmd = 'svn log -v --xml %s > %s '%(repo_trunk, log_file)
    # if os.system(cmd) == 0:
    #     logger.info('succ gen log for ', project)
    # else:
    #     logger.warning('FAILED gen log for ', project)
    logger.info(os.popen(cmd))

    logger.info('----------stats  ..................')
    cmd = 'java -jar %s %s %s -output-dir %s '%(stat_cmd, log_file, repo_trunk, rept_dir)
    # if os.system(cmd) == 0:
    #     logger.info('succ gen stats for ', project)
    # else:
    #     logger.warning('FAILED gen stats for ', project)
    logger.info(os.popen(cmd))

def main():
    statsvn()

if __name__=="__main__":
    main()