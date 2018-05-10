#!/bin/bash

# winnerrxd  --> rxd
prj=$Project
shortname=${prj:6}

echo "###################开始自动部署##################"
	tomcatpath=/usr/tomcats/apache-tomcat-7.0-${shortname}/webapps
	backuppath=/usr/tomcats/backup/${shortname}
	deploy=/usr/tomcats/backup/deploy
	date=`(date "+%Y-%m-%d_%H-%M-%S")`
	#chown -R tomcat:tomcat /data/

echo "开始关闭Tomcat"
	service tomcat${shortname} stop
		 sleep 1
	pid=`(ps -ef|grep apache-tomcat-7.0-${shortname} |grep -v root|awk '{print $2}')`
	if [ ! -n "$pid" ]
	then 
		 echo "tomcat 关闭成功 "
	else
		echo   "tomcat 关闭失败,强制关闭"
		kill -9 $pid
	 fi

echo "开始解压.................."
	# rm -rf $tomcatpath/winner${shortname}.war
	rm -rf $tomcatpath/winner${shortname}
	unzip $deploy/winner${shortname}.war -d $tomcatpath/winner${shortname}/ >/dev/null 2>&1
echo "解压完成，开始部署"

echo "修改用户"
	chown -R tomcat:tomcat $tomcatpath

echo "启动服务"
	service tomcat${shortname} start
echo "##################部署完成，请验证是否发布成功####################"

exit
