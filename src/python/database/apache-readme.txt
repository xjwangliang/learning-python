Mac OS X 内置Apache 和 PHP，使用起来非常方便。本文以Mac OS X 10.6.3和 10.8.1为例。主要内容包括：
启动Apache

有两种方法：

    打开“系统设置偏好（System Preferences）” -> “共享（Sharing）” -> “Web共享（Web Sharing）”。注意，从Mac OS X从10.8开始取消了 “Web共享（Web Sharing）”。
    打开“终端（terminal）”，然后（注意，sudo需要的密码就是系统的root帐号密码）
        运行“sudo apachectl start”，再输入帐号密码，这样Apache就运行了。
        运行“sudo apachectl －v”，你会看到Mac OS X的Apache版本信息，如10.8.1中：

        Server version: Apache/2.2.22 (Unix)
        Server built:   Jun 20 2012 13:57:09
        
        
        
如此在浏览器中输入“http://localhost”，就可以看到一个内容为“It works!”的页面，其位于“/Library（资源库）/WebServer/Documents/”下，这就是Apache的默认根目录。

注意：开启了Apache就是开启了“Web共享”，这时联网用户就会通过“http://[本地IP]/”来访问“/Library（资源库）/WebServer/Documents/”目录，通过“http://[本地IP]/~[用户名]”来访问“/Users/[用户名]/Sites/”目录。值得注意的是，Mac OS X在10.8中取消”Web共享（Web Sharing）”时，也移除了“/Users/[用户名]/Sites/”目录，所以10.8中访问“http://[本地IP]/~[用户名]”会显示“403 Forbidden”，但http://[本地IP]/依旧可以访问。可以到“系统偏好设置” -> “安全（Security）” -> “防火墙（Firewall）”，开启防火墙，然后在“防火墙选项（Firewall Options）”中勾上“组织所有进入连接（block all incoming connections）”即可。也可以通过设置httpd.conf来只允许localhost和127.0.0.1访问“/Library（资源库）/WebServer/Documents/”。
/etc/apache2/httpd.conf

<Directory "/Library/WebServer/Documents">
    ......
    #
    # Controls who can get stuff from this server.
    #
    Order allow,deny
    #Allow from all
    Allow from 127.0.0.1
    Allow from localhost 

</Directory>



一定要系统设置偏好（System Preferences）” -> “共享（Sharing）” -> “Web共享（Web Sharing）选中
http://localhost/postgresql/html/
(/Library/WebServer/Documents)
http://localhost/~wangliang	
(/Users/wangliang/Sites)




在终端中运行“sudo vi /etc/apache2/httpd.conf”，打开Apache的配置文件。（如果不习惯操作终端和vi，可以设置在Finder中显示所有系统隐藏文件，记得设置完毕后需要重启Finder，然后就可以找到对应文件，随心所欲编辑了，需要注意的是某些文件的修改还是需要开启root帐号，但整体上还是在终端上使用sudo来临时获取root权限比较安全。）
找到“#LoadModule php5_module libexec/apache2/libphp5.so”，把前面的#号去掉，保存（在命令行输入:w）并退出vi（在命令行输入:q）。

运行“sudo apachectl restart”，重启Apache，这样PHP就可以用了。
运行“sudo cp /Library/WebServer/Documents/index.html.en /Library/WebServer/Documents/info.php”，即在Apache的根目录下复制index.html.en文件并重命名为info.php。

设置虚拟主机

    在终端运行“sudo vi /etc/apache2/httpd.conf”，打开Apche的配置文件
    在httpd.conf中找到“#Include /private/etc/apache2/extra/httpd-vhosts.conf”，去掉前面的“＃”，保存并退出。
    运行“sudo apachectl restart”，重启Apache后就开启了虚拟主机配置功能。
    运行“sudo vi /etc/apache2/extra/httpd-vhosts.conf”，就打开了配置虚拟主机文件httpd-vhost.conf，配置虚拟主机了。需要注意的是该文件默认开启了两个作为例子的虚拟主机：

    <VirtualHost *:80>
        ServerAdmin webmaster@dummy-host.example.com
        DocumentRoot "/usr/docs/dummy-host.example.com"
        ServerName dummy-host.example.com
        ErrorLog "/private/var/log/apache2/dummy-host.example.com-error_log"
        CustomLog "/private/var/log/apache2/dummy-host.example.com-access_log" common
    </VirtualHost>

    <VirtualHost *:80>
        ServerAdmin webmaster@dummy-host2.example.com
        DocumentRoot "/usr/docs/dummy-host2.example.com"
        ServerName dummy-host2.example.com
        ErrorLog "/private/var/log/apache2/dummy-host2.example.com-error_log"
        CustomLog "/private/var/log/apache2/dummy-host2.example.com-access_log" common
    </VirtualHost> 

    而实际上，这两个虚拟主机是不存在的，在没有配置任何其他虚拟主机时，可能会导致访问localhost时出现如下提示：

    Forbidden
    You don't have permission to access /index.php on this server

    最简单的办法就是在它们每行前面加上#，注释掉就好了，这样既能参考又不导致其他问题。
    增加如下配置

    <VirtualHost *:80>
        DocumentRoot "/Library/WebServer/Documents"
        ServerName localhost
        ErrorLog "/private/var/log/apache2/localhost-error_log"
        CustomLog "/private/var/log/apache2/localhost-access_log" common
    </VirtualHost> 

    <VirtualHost *:80>
        DocumentRoot "/Users/[用户名]/Sites"
        ServerName sites
        ErrorLog "/private/var/log/apache2/sites-error_log"
        CustomLog "/private/var/log/apache2/sites-access_log" common
        <Directory />
                    Options Indexes FollowSymLinks MultiViews
                    AllowOverride None
                    Order deny,allow
                    Allow from all
          </Directory>
    </VirtualHost> 

    保存退出，并重启Apache。
    运行“sudo vi /etc/hosts”，打开hosts配置文件，加入"127.0.0.1 sites"，这样就可以配置完成sites虚拟主机了，可以访问“http://sites”了，在10.8之前Mac OS X版本其内容和“http://localhost/~[用户名]”完全一致。
    注意，记录log的“ErrorLog "/private/var/log/apache2/sites-error_log"”也可以删掉，但记录日志其实是一个好习惯，在出现问题时可以帮助我们判断。如果保留这些log代码，一定log文件路径都是存在的，如果随便修改一个不存在的，会导致Apache无法服务而没有错误提示，这个比较恶心。

这里利用Mac OS X 10.6.3和10.8.1中原生支持的方式来实现的配置，也可以参考“Mac OS X Leopard: 配置Apache, PHP, SQLite, MySQL, and phpMyAdmin(一) ”和“Mac OS X Leopard: 配置Apache, PHP, SQLite, MySQL, and phpMyAdmin(二) ”。实际上，还可以使用XAMPP或MacPorts这种第三方提供的集成方案来实现简单的安装和使用。


参考
http://dancewithnet.com/2010/05/09/run-apache-php-mysql-in-mac-os-x/




当你在 Mac OS X 下启用了 Web Sharing，其实就是 Apache2 服务, 到浏览器里访问 http://localhost/~{username} 时提示

Forbidden

You don't have permission to access /~{username}/ on this server.

{username} 代表当前系统用户名。

看到上面的问题，首先会想到的是目录下 /Users/{username}/Sites 下的文件权限问题，有可能，但我碰到的问题不是这样的。

而是需要在目录 /etc/apache2/users 创建一个文件 {username}.conf，如 Unmi.conf，甚至可以任意文件名，文件内容如下：

	
<Directory "/Users/{username}/Sites/">
    Options Indexes MultiViews
    AllowOverride AuthConfig Limit
    Order allow,deny
    Allow from all
</Directory>

最后，在 System Preferences 里重新启动下 Web Sharing 就可以解决了。

注意，系统升级到最新的 Mountain Lion 之后，在 System Preferences 里已经没有 Web Sharing 项目，你必须在命令行下用命令
1
	
sudo apachectl start/stop/restart/graceful

参考http://unmi.cc/2012/07

