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





在终端中运行“sudo vi /etc/apache2/httpd.conf”，打开Apache的配置文件。（如果不习惯操作终端和vi，可以设置在Finder中显示所有系统隐藏文件，记得设置完毕后需要重启Finder，然后就可以找到对应文件，随心所欲编辑了，需要注意的是某些文件的修改还是需要开启root帐号，但整体上还是在终端上使用sudo来临时获取root权限比较安全。）
找到“#LoadModule php5_module libexec/apache2/libphp5.so”，把前面的#号去掉，保存（在命令行输入:w）并退出vi（在命令行输入:q）。

运行“sudo apachectl restart”，重启Apache，这样PHP就可以用了。
运行“sudo cp /Library/WebServer/Documents/index.html.en /Library/WebServer/Documents/info.php”，即在Apache的根目录下复制index.html.en文件并重命名为info.php。


参考
http://dancewithnet.com/2010/05/09/run-apache-php-mysql-in-mac-os-x/



