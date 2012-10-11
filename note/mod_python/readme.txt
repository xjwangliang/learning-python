下载mod_python源码，进入根目录
>>>>>>>>./configure --with-apxs=/usr/local/apache2/bin/apxs --with-python=/usr/local/bin/python

注意apache2安装在/usr/local/apache2目录，这里指定到是apxs到路径，后者可以不指定（从PATH中寻找可执行到python：/usr/local/bin/python,但是python是在/usr/local/lib/python2.7）

>>>>>>>>>>make
注意这一步会出错

connobject.c: In function ‘_conn_read’:
connobject.c:142:19: error: request for member ‘next’ in something not a structure or union
apxs:Error: Command failed with rc=65536

改正：



diff -rNu mod_python-3.3.1/src/connobject.c mod_python-3.3.1-atomix/src/connobject.c
--- mod_python-3.3.1/src/connobject.c	2006-12-03 05:36:37.000000000 +0100
+++ mod_python-3.3.1-atomix/src/connobject.c	2008-10-02 14:10:02.000000000 +0200
@@ -139,7 +139,7 @@
     bytes_read = 0;
 
     while ((bytes_read < len || len == 0) &&
-           !(b == APR_BRIGADE_SENTINEL(b) ||
+           !(b == APR_BRIGADE_SENTINEL(bb) ||
              APR_BUCKET_IS_EOS(b) || APR_BUCKET_IS_FLUSH(b))) {
 
         const char *data;

也就是说，在mod_python-3.3.1/src/connobject.c 源文件中将!(b == APR_BRIGADE_SENTINEL(b) ||替换为!(b == APR_BRIGADE_SENTINEL(bb) ||（在142行），然后重新make

>>>>>>>>>>>>sudo make install

这样会在apache2到modules目录中生成mod_python.so文件，并且在python安装位置生成目录（ /usr/local/lib/python2.7/dist-packages/mod_python）


配置
在apache2的conf目录的httpd.conf文件中按照以下方式：（这是在make install后输出的）
Now don't forget to edit your main config and add
    LoadModule python_module /usr/local/apache2/modules/mod_python.so
and if your configuration uses ClearModuleList, then also
    AddModule mod_python.c



htdocs目录是项目目录


./httpd -M
