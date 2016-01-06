## windows开发环境搭建：##

----------

安装python3.5,设置python ->Path
下载安装：distribute
安装pip,python get-pip.py
django安装：pip install django
django加入环境变量
PyMySQL ：pip install PyMySQL

## django命令： ##

----------

新建项目：django-damin.py startproject project-name
项目下新建app: python manage.py startapp app-namem

在setting加入数据库链接参数后同步：
python manage.py makemigrations
python manage.py migrate
python manage.py runserver ip:port
python manage.py createsuperuser 
## linux环境搭建： ##

----------

升级python,保留原来的python版本
ls -n /usr/local/python3.5/bin/python.3.5 /usr/bin/python
查看版本号：pathon -V
安装distribute
安装pip
安装pip,python get-pip.py
django安装：pip install django
django加入环境变量
安装生产环境：lnmp集成环境
pip install uwsgi


## 前端：Bootstrap ##

----------



killall -9 uwsgi
netstat -tap |grep mysql
lsof -i :port端口号

## 学员课程管理 ##

qq:312062001
微信：spring3th

