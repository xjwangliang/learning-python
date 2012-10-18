

Due to a bug in the Mac OS X package installer, you may see this error
message in the destination disk selection dialog:

     You cannot install this software on this disk. (null)

If this error occurs, simply click the `Go Back' button once to return
to the previous screen. Then click `Continue' to advance to the
destination disk selection again, and you should be able to choose the
destination disk correctly. We have reported this bug to Apple and it is
investigating this problem.

The Mac OS X PKG of MySQL installs itself into
`/usr/local/mysql-VERSION' and also installs a symbolic link,
`/usr/local/mysql', that points to the new location. If a directory
named `/usr/local/mysql' exists, it is renamed 
`/usr/local/mysql.bak' first. Additionally, the installer creates the
grant tables in the `mysql' database by executing `mysql_install_db'.

The installation layout is similar to that of a `tar' file binary
distribution; all MySQL binaries are located in the directory
`/usr/local/mysql/bin'. The MySQL socket file is created as
`/tmp/mysql.sock' by default. See *Note installation-layouts::.

MySQL installation requires a Mac OS X user account named `mysql'. A
user account with this name should exist by default on Mac OS X 10.2
and up.

If you are running Mac OS X Server, a version of MySQL should already
be installed. The following table shows the versions of MySQL that ship
with Mac OS X Server versions.

*Mac OS X Server       *MySQL Version*
Version*               
10.2-10.2.2            3.23.51
10.2.3-10.2.6          3.23.53
10.3                   4.0.14
10.3.2                 4.0.16
10.4.0                 4.1.10a


If you want MySQL to start automatically during system startup, you
also need to install the MySQL Startup Item. It is part of the Mac OS X
installation disk images as a separate installation package. Simply
double-click the `MySQLStartupItem.pkg' icon and follow the
instructions to install it. The Startup Item need be installed only
once. There is no need to install it each time you upgrade the MySQL
package later.

The Startup Item for MySQL is installed into
`/Library/StartupItems/MySQLCOM'. (Before MySQL 4.1.2, the location was
`/Library/StartupItems/MySQL', but that collided with the MySQL Startup
Item installed by Mac OS X Server.) Startup Item installation adds a
variable `MYSQLCOM=-YES-' to the system configuration file
`/etc/hostconfig'. If you want to disable the automatic startup of
MySQL, simply change this variable to `MYSQLCOM=-NO-'.
------------------------------------------------------------------------------
`/Library/StartupItems/MySQLCOM'
`/Library/StartupItems/MySQL'
/etc/hostconfig
(MYSQLCOM=-YES-  MYSQLCOM=-NO-)
------------------------------------------------------------------------------




After the installation, you can start up MySQL by running the following
commands in a terminal window. You must have administrator privileges
to perform this task.

If you have installed the Startup Item, use this command:

     shell> sudo /Library/StartupItems/MySQLCOM/MySQLCOM start
     (ENTER YOUR PASSWORD, IF NECESSARY)
     (PRESS CONTROL-D OR ENTER "EXIT" TO EXIT THE SHELL)

If you don't use the Startup Item, enter the following command sequence:

     shell> cd /usr/local/mysql
     shell> sudo ./bin/mysqld_safe
     (ENTER YOUR PASSWORD, IF NECESSARY)
     (PRESS CONTROL-Z)
     shell> bg
     (PRESS CONTROL-D OR ENTER "EXIT" TO EXIT THE SHELL)

You should be able to connect to the MySQL server, for example, by
running `/usr/local/mysql/bin/mysql'.

*Note*: The accounts that are listed in the MySQL grant tables
initially have no passwords.  After starting the server, you should set
up passwords for them using the instructions in *Note
post-installation::.

You might want to add aliases to your shell's resource file to make it
easier to access commonly used programs such as `mysql' and
`mysqladmin' from the command line. The syntax for `bash' is:

     alias mysql=/usr/local/mysql/bin/mysql
     alias mysqladmin=/usr/local/mysql/bin/mysqladmin

For `tcsh', use:

     alias mysql /usr/local/mysql/bin/mysql
     alias mysqladmin /usr/local/mysql/bin/mysqladmin

Even better, add `/usr/local/mysql/bin' to your `PATH' environment
variable. You can do this by modifying the appropriate startup file for
your shell. For more information, see *Note invoking-programs::.

If you are upgrading an existing installation, note that installing a
new MySQL PKG does not remove the directory of an older installation.
Unfortunately, the Mac OS X Installer does not yet offer the
functionality required to properly upgrade previously installed
packages.

To use your existing databases with the new installation, you'll need
to copy the contents of the old data directory to the new data
directory. Make sure that neither the old server nor the new one is
running when you do this. After you have copied over the MySQL database
files from the previous installation and have successfully started the
new server, you should consider removing the old installation files to
save disk space. Additionally, you should also remove older versions of
the Package Receipt directories located in
`/Library/Receipts/mysql-VERSION.pkg'.

