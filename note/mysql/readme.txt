安装mysql
sudo apt-get install mysql-server mysql-client #中途会让你输入一次root用户密码

启动服务
sudo start mysql #手动的话这样启动
当你修改了配置文件後，你需要重启 mysqld 才能使这些修改生效。

要想检查 mysqld 进程是否已经开启
pgrep mysqld  返回进程到id 



wang@ubuntu:~/Desktop/android$ which mysql
/usr/bin/mysql

配置文件/etc/mysql/my.cnf 
datadir         = /var/lib/mysql指定数据库文件路径
所以如果你创建了一个名为 test 的数据库，那么这个数据库的数据会存放到 /var/lib/mysql/test 目录下


mysql -uroot(username) -pwang(password)
修改密码
sudo mysqladmin -u root password newpassword；


以后找文件，请用：locate mysql

执行文件
/usr/bin/mysql

数据库
/var/lib/mysql

/var/log/mysql

控制文件
/etc/mysql/my.cnf

祝福安好

参考
http://wiki.ubuntu.com.cn/MySQL
