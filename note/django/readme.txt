python:
/usr/bin/python

git clone https://github.com/django/django.git
enter source dirctory and run 
sudo python setup.py install

django in:
/usr/local/lib/python2.7/dist-packages/django/
查看安装路径（不是python shell）
python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"
['/usr/local/lib/python2.7/dist-packages/django']

删除这个目录就是删除django


in python terminal:
	import django
	  

或者
python -c "import django; print(django.get_version())"




创建一个项目
django-admin.py startproject mysite（项目名称）

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py


hese files are:

    The outer mysite/ directory is just a container for your project. Its name doesn't matter to Django; you can rename it to anything you like.
    manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin.py and manage.py.
    The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you'll need to use to import anything inside it (e.g. import mysite.settings).
    mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. (Read more about packages in the official Python docs if you're a Python beginner.)
    mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
    mysite/urls.py: The URL declarations for this Django project; a "table of contents" of your Django-powered site. You can read more about URLs in URL dispatcher.
    mysite/wsgi.py: An entry-point for WSGI-compatible webservers to serve your project. See How to deploy with WSGI for more details.

有两个叫做mysite的目录，进入外层目录，运行
python manage.py runserver
然后输出
Development server is running at http://127.0.0.1:8000/
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000


浏览器输出结果
	
	Of course, you haven't actually done any work yet. Here's what to do next:
	If you plan to use a database, edit the DATABASES setting in DJ/settings.py.
	Start your first app by running python manage.py startapp [appname].
	You're seeing this message because you have DEBUG = True in your Django settings file and you haven't configured any URLs. Get to work!


安装好mysql-python之后，运行
python manage.py syncdb

注意：在外层目录中运行；需要更改setting.py的设置：

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mydb	',                      # Or path to database file if using sqlite3.数据库到名字，事先在mysql中创建
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'wang',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}
运行过程
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (leave blank to use u'wang'): root
E-mail address: wsl906@sina.com
Password: wang
Password (again): wang
Superuser created successfully.
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)


查看数据库
mysql> use mydb ;
Database changed
mysql> show tables ;
+----------------------------+
| Tables_in_mydb             |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_content_type        |
| django_session             |
| django_site                |
+----------------------------+
9 rows in set (0.01 sec)

mysql> select * from auth_user ;
+----+----------+------------+-----------+-----------------+-------------------------------------------------------------------------------+----------+-----------+--------------+---------------------+---------------------+
| id | username | first_name | last_name | email           | password                                                                      | is_staff | is_active | is_superuser | last_login          | date_joined         |
+----+----------+------------+-----------+-----------------+-------------------------------------------------------------------------------+----------+-----------+--------------+---------------------+---------------------+
|  1 | root     |            |           | wsl906@sina.com | pbkdf2_sha256$10000$7K7XNolSFP9A$mEX8wt/GCiLbEYPdDdo1fwK+xZP/o5o8Ohf8t4iWlkw= |        1 |         1 |            1 | 2012-09-25 17:39:31 | 2012-09-25 17:39:31 |
+----+----------+------------+-----------+-----------------+-------------------------------------------------------------------------------+----------+-----------+--------------+---------------------+---------------------+
1 row in set (0.01 sec)

参考https://docs.djangoproject.com/en/dev/intro/tutorial01/

