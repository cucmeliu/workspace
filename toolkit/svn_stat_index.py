#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: svn_backup
# author: leo.liu
# date: 2018.5.10

import os

projects=[
'35DbLocal', 
'41SmartCallCenter', 
'50winnerClean', 
'60Cloud', '60winnerMonitor', '61winnerCommon', 
'62BI', 
'70IoTreveal',
'winnerMasServer', 'winnerSMS', 'winnerSMS-api', 'winnerSMS-sms', 'winnerVoiceNew']

no_trunk_projects=['10winnerhome', 
'docs', 'incubator',
'yes云信', '高速触发管理平台']

# 报告首页，项目列表
idx_file    = 'F:\\backuprep\\reports\index.html'


def buildindex():
    allProject = projects
    allProject.extend(no_trunk_projects)
    str = '<head><title>代码量统计台</title></head>'
    str = str + '<body>'
    str = str + '<h1>代码量统计台</h1>'
    str = str + '<ul>'
    for project in allProject:
        str = str + '<li><a href="%s" > %s </a></li>'%(project, project) 
    str = str + '</ul>'
    str = str + '</body>'

    with open(idx_file.decode('utf-8').encode('gb2312'), 'wb') as f:
        f.write(str.decode('utf-8').encode('gb2312'))

def main():
    print 'build index page...'
    buildindex()
    print 'done'

if __name__=="__main__":
    main()