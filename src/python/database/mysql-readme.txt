   To install and use a MySQL binary distribution, the basic command
   sequence looks like this:
shell> groupadd mysql
shell> useradd -r -g mysql mysql
shell> cd /usr/local
shell> tar zxvf /path/to/mysql-VERSION-OS.tar.gz
shell> ln -s full-path-to-mysql-VERSION-OS mysql
shell> cd mysql
shell> chown -R mysql .
shell> chgrp -R mysql .
shell> scripts/mysql_install_db --user=mysql
shell> chown -R root .
shell> chown -R mysql data
# Next command is optional
shell> cp support-files/my-medium.cnf /etc/my.cnf
shell> bin/mysqld_safe --user=mysql &
# Next command is optional
shell> cp support-files/mysql.server /etc/init.d/mysql.server


按照这个也不成功



MAC 上安装MYSQL
MBP 自带的系统有有apache ,php,python  但是没有mysql ,于是需要自己倒腾下。‘倒腾’这词用得好，因为我的确倒腾了好久。 
刚开始用brew search mysql ...能找到，按照提示一步一步安装，结果到最后就是启动不起来，老提示一个sock相关的错误。。

后来我还是直接到mysql 的官网下载了适合MAC 平台的 mysql-5.5.17-osx10.6-x86_64.dmg 

打开后发现3个文件，安装顺序：

1。mysql-5.5.17-osx10.6-x86_64.pkg 数据库
2。MySQLStartupItem.pkg 这样MySQL就会自动在开机时自动启动了。
3。MySQL.prefPane  这样就会在“系统设置偏好”中看到名为“MySQL”的ICON，通过它就可以设置MySQL开始还是停止，以及是否开机时自动运行。到这里MySQL就基本安装完毕了。

通过运行“sudo vi /etc/bashrc”，在bash的配置文件中加入mysql和mysqladmin的别名

#mysql

alias mysql='/usr/local/mysql/bin/mysql'

alias mysqladmin='/usr/local/mysql/bin/mysqladmin'

或者
#mysql
alias mysqlstart='sudo /Library/StartupItems/MySQLCOM/MySQLCOM restart'
alias mysql='/usr/local/mysql/bin/mysql'
alias mysqladmin='/usr/local/mysql/bin/mysqladmin'

这样就可以在终端中比较简单地通过命令进行相应的操作，比如安装完毕之后MySQL的root默认密码为空，如果要设置密码可以在终端运行“mysqladmin -u root password "mysqlpassword"”来设置，其中mysqlpassword即root的密码。

备注：使用PHP连接MySQL可能会报错“Can’t connect to local MySQL server through socket ‘/var/mysql/mysql.sock’”，或者使用localhost无法连接MySQL而需要127.0.0.1，原因是连接时候php默认去找/var/mysql/mysql.sock了，但是MAC版本的MYSQL改动了文件的位置，放在/tmp下了。处理办法是按如下修改php.ini：


注意：Mac OS X的升级或其他原因可能会导致ＭySQL启动或开机自动运行时，在ＭySQL操作面板上会提示“Warning:The /usr/local/mysql/data directory is not owned by the 'mysql' or '_mysql' ”，这应该是某种情况下导致/usr/local/mysql/data的宿主发生了改变，只需要运行“sudo chown -R mysql /usr/local/mysql/data”即可。


mysql.default_socket = /tmp/mysql.sock

参考http://www.blogjava.net/JAVA-HE/archive/2011/11/04/362717.html

http://dancewithnet.com/2010/05/09/run-apache-php-mysql-in-mac-os-x/
http://www.cnblogs.com/macro-cheng/archive/2011/10/25/mysql-001.html
、

设置密码
http://dev.mysql.com/doc/refman/5.5/en/resetting-permissions.html
auto-increment()
http://dev.mysql.com/doc/refman/5.0/en/example-auto-increment.html

插入多条记录
（１）INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');
    
    
 插入多条记录
 （2）
 CREATE TABLE animals (
    grp ENUM('fish','mammal','bird') NOT NULL,
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (grp,id)
) ENGINE=MyISAM;

INSERT INTO animals (grp,name) VALUES
    ('mammal','dog'),('mammal','cat'),
    ('bird','penguin'),('fish','lax'),('mammal','whale'),
    ('bird','ostrich');

mysql数据类型
http://www.cnblogs.com/macro-cheng/archive/2011/10/26/mysql-002.html

09-29 15:57:08.400: E/AndroidRuntime(16239): Caused by: java.lang.IndexOutOfBoundsException: Invalid index 0, size is 0
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at java.util.ArrayList.throwIndexOutOfBoundsException(ArrayList.java:251)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at java.util.ArrayList.get(ArrayList.java:304)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.data.db.NormalCardDao.savePopulars(NormalCardDao.java:97)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.service.CardService.savePoppulars(CardService.java:207)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.service.CardService.getAllPopular(CardService.java:281)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.activity.Popular.getCards(Popular.java:617)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.activity.Popular.access$8(Popular.java:613)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.activity.Popular$8.doInBackground(Popular.java:543)
09-29 15:57:08.400: E/AndroidRuntime(16239): 	at com.guoku.activity.BaseAdapterActivity$LoadDataTask.doInBackground(BaseAdapterActivity.java:1)


09-29 16:02:33.470: E/AndroidRuntime(17451): java.lang.RuntimeException: Unable to instantiate application com.guoku.activity.ApplicationEx: java.lang.NullPointerException
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.LoadedApk.makeApplication(LoadedApk.java:482)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.ActivityThread.handleBindApplication(ActivityThread.java:3955)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.ActivityThread.access$1300(ActivityThread.java:127)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1196)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.os.Handler.dispatchMessage(Handler.java:99)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.os.Looper.loop(Looper.java:137)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.ActivityThread.main(ActivityThread.java:4441)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at java.lang.reflect.Method.invokeNative(Native Method)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at java.lang.reflect.Method.invoke(Method.java:511)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:823)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:590)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at dalvik.system.NativeStart.main(Native Method)
09-29 16:02:33.470: E/AndroidRuntime(17451): Caused by: java.lang.NullPointerException
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.LoadedApk.initializeJavaContextClassLoader(LoadedApk.java:362)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.LoadedApk.getClassLoader(LoadedApk.java:305)
09-29 16:02:33.470: E/AndroidRuntime(17451): 	at android.app.LoadedApk.makeApplication(LoadedApk.java:474)


请求：api_key=0b19c2b93687347e95c6b6f5cc91bb87&page=1&sign=865fd44a427d97212a407b88c83e9b87&size=60&type=pop_d


select * from favor_list_category;

select * from favor_list;
 
A) If you are using mysql on RedHat Linux (Fedora Core/Cent OS) then use following command:

* To start mysql server:

/etc/init.d/mysqld start
* To stop mysql server:

/etc/init.d/mysqld stop
* To restart mysql server

 /etc/init.d/mysqld restart
Tip: Redhat Linux also supports service command, which can be use to start, restart, stop any service:

# service mysqld start
# service mysqld stop
# service mysqld restart
(B) If you are using mysql on Debian / Ubuntu Linux then use following command:

* To start mysql server:

/etc/init.d/mysql start
* To stop mysql server:

/etc/init.d/mysql stop

* To restart mysql server
/etc/init.d/mysql restart
http://theos.in/desktop-linux/tip-that-matters/how-do-i-restart-mysql-server/
