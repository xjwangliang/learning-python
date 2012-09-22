对于mysql
.. ERROR! The server quit without updating PID file (/usr/local/var/mysql/wang.pid).
vi /usr/local/var/mysql/wang.err
chown -R wangliang /usr/local/var/mysql/
>>>>>>>>>>>>>>>>>>>>
cd /usr/local/Cellar/mysql/5.5.20/
/usr/local/Cellar/mysql/5.5.20/scripts/mysql_install_db

Installing MySQL system tables...
OK
Filling help tables...
OK

To start mysqld at boot time you have to copy
support-files/mysql.server to the right place for your system

PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:

./bin/mysqladmin -u root password 'new-password'
./bin/mysqladmin -u root -h wang password 'new-password'

Alternatively you can run:
./bin/mysql_secure_installation

which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.

See the manual for more instructions.

You can start the MySQL daemon with:
cd . ; ./bin/mysqld_safe &

You can test the MySQL daemon with mysql-test-run.pl
cd ./mysql-test ; perl mysql-test-run.pl
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




安装pymongo（http://api.mongodb.org/python/2.0.1/installation.html/http://api.mongodb.org/python/2.3/installation.html）

我使用源码安装

$ git clone git://github.com/mongodb/mongo-python-driver.git pymongo
$ cd pymongo/
$ python setup.py install

最后一句可能没有权限，可能需要加上sudo
（在源码目录创建build目录（编译的文件放在字目录下），然后编译，最后拷贝到/Library/Python/2.7/site-packages（pymongo-2.3_-py2.7-macosx-10.7-intel.egg）


在python命令行中执行import pymongo，没有出错就表示安装成功


安装mongo
下载解压得到（并且只有目录>170M）mongodb-osx-x86_64-2.2.0/bin,里面有很多命令
将bin目录添加到path

运行mongod
可以看到输出MongoDB starting : pid=524 port=27017 dbpath=/data/db/ 64-bit host=wang
，dbpath=/data/db/ 所以可能出错，因为/data/db/可能并不存在（http://dochub.mongodb.org/core/startingandstoppingmongo）

mongod --dbpath /Users/wangliang/Documents/python/mongo-work/db1

mongod --help

输出为
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
wang:mongo-work wangliang$ mongod  --dbpath /Users/wangliang/Documents/python/mongo-work/db1
MongoDB starting : pid=527 port=27017 dbpath=/Users/wangliang/Documents/python/mongo-work/db1 64-bit host=wang

** WARNING: soft rlimits too low. Number of files is 256, should be at least 1000
db version v2.2.0, pdfile version 4.5
git version: f5e83eae9cfbec7fb7a071321928f00d1b0c5207
build info: Darwin bs-osx-106-x86-64-1.local 10.8.0 Darwin Kernel Version 10.8.0: Tue Jun  7 16:33:36 PDT 2011; root:xnu-1504.15.3~1/RELEASE_I386 i386 BOOST_LIB_VERSION=1_49
options: { dbpath: "/Users/wangliang/Documents/python/mongo-work/db1" }
journal dir=/Users/wangliang/Documents/python/mongo-work/db1/journal
recover : no journal files present, no recovery needed
Sat Sep 22 11:05:56 [websvr] admin web console waiting for connections on port 28017
waiting for connections on port 27017
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





#mongo自动创建db，插入数据之后才创建，如果查询不存在的db，那么会创建一个空的db

mongo操作
show dbs;
show tables;
db.system.indexes.find() db.things.getIndexes()


# As soon as you insert something, MongoDB creates the underlying collection and database. If you query a collection that does not exist, MongoDB treats it as an empty collection.
use mydb	
j = { name : "mongo" };
db.things.save(j);		#插入
db.things.find();		#查询
for (var i = 1; i <= 20; i++) db.things.save({x : 4, j : i});#Type "it" for more

迭代
var cursor = db.things.find();
while (cursor.hasNext()) printjson(cursor.next());

迭代
db.things.find().forEach(printjson);




> var cursor = db.things.find();
> printjson(cursor[4]);				＃取出第三条数据


> var arr = db.things.find().toArray();
> arr[5];



查询
＃SELECT * FROM things WHERE name="mongo"
db.things.find({name:"mongo"}).forEach(printjson);db.things.find({x:4}).forEach(printjson);
＃A query document of the form { a:A, b:B, ... } means "where a==A and b==B and ...".

// retrieve ssn field for documents where last_name == 'Smith':
db.users.find({last_name: 'Smith'}, {'ssn': 1});

// retrieve all fields *except* the thumbnail field, for all documents:
db.users.find({}, {thumbnail:0});
  
＃SELECT j FROM things WHERE x=4
db.things.find({x:4}, {j:true}).forEach(printjson);
＃Note that the "_id" field is always returned.


#查询第一行
printjson(db.things.findOne({name:"mongo"}));相当于find({name:"mongo"}).limit(1).
printjson(db.things.find({x:4})[0]);
printjson(db.things.findOne({x:4}));
db.things.find({x:4}).limit(1);		#printjson结果不一样


var doc = db.things.findOne({_id:ObjectId("4c2209f9f3924d31102bd84a")});
doc

＃查询前３条
db.things.find().limit(3);

db.users.find().skip(20).limit(10);
db.users.find({}, {}, 10, 20); // same as above, but less clear


cursor一条数据、数组一条元素
printjson(cursor.next())
printjson(cursor[4]);
printjson(findOne);



CREATE TABLE USERS (a Number, b Number)					db.createCollection("mycoll"或者隐式
INSERT INTO USERS VALUES(3,5)							db.users.insert({a:3,b:5})
SELECT a,b FROM users									db.users.find({}, {a:1,b:1})					//这样会查询所有的行，没有a、b字段的就不会显示a、b字段
SELECT a,b FROM users WHERE age=33						db.users.find({age:33}, {a:1,b:1})
SELECT * FROM users WHERE age=33 ORDER BY name			db.users.find({age:33}).sort({name:1})			//排序
SELECT * FROM users WHERE age>33						db.users.find({age:{$gt:33}})
SELECT * FROM users WHERE age!=33						db.users.find({age:{$ne:33}})
SELECT * FROM users WHERE name LIKE "%Joe%"				db.users.find({name:/Joe/})
SELECT * FROM users WHERE name LIKE "Joe%"				db.users.find({name:/^Joe/})
SELECT * FROM users WHERE age>33 AND age<=40			db.users.find({'age':{$gt:33,$lte:40}})
SELECT * FROM users ORDER BY name DESC					db.users.find().sort({name:-1})
SELECT * FROM users LIMIT 10 SKIP 20					db.users.find().limit(10).skip(20)
SELECT * FROM users WHERE a=1 or b=2					db.users.find( { $or : [ { a : 1 } , { b : 2 } ] } )
SELECT * FROM users LIMIT 1								db.users.findOne()


SELECT order_id FROM orders o, order_line_items li WHERE li.order_id=o.order_id AND li.sku=12345				db.orders.find({"items.sku":12345},{_id:1})			??

SELECT customer.name FROM customers,orders WHERE orders.id="q179" AND orders.custid=customer.id					var o = db.orders.findOne({_id:"q179"});var name = db.customers.findOne({_id:o.custid})
SELECT DISTINCT last_name FROM users																			db.users.distinct('last_name')
SELECT COUNT(*)	FROM users																						db.users.count()
SELECT COUNT(*) FROM users where AGE > 30																		db.users.find({age: {'$gt': 30}}).count()
SELECT COUNT(AGE) from users																					db.users.find({age: {'$exists': true}}).count()


CREATE INDEX myindexname ON users(name)						db.users.ensureIndex({name:1})						//索引
CREATE INDEX myindexname ON users(name,ts DESC)				db.users.ensureIndex({name:1,ts:-1})
UPDATE users SET a=1 WHERE b='q'							db.users.update({b:'q'}, {$set:{a:1}}, false, true)
UPDATE users SET a=a+2 WHERE b='q'							db.users.update({b:'q'}, {$inc:{a:2}}, false, true)
DELETE FROM users WHERE z="abc"								db.users.remove({z:'abc'});


执行函数
> var cur = db.example.find();
> cur.forEach( function(x) { print(tojson(x))})

插入
> db.things.insert( { name: "xyz", metro: { city: "New York", state: "NY" } } );
> db.things.find({metro:{'$exists':1}});

索引http://www.mongodb.org/display/DOCS/Indexes
db.factories.insert( { name: "xyz", metro: { city: "New York", state: "NY" } } );
db.factories.ensureIndex( { metro : 1 } );
// this query can use the above index:
db.factories.find( { metro: { city: "New York", state: "NY" } } );
// this one too, as {city:"New York"} < {city:"New York",state:"NY"}
db.factories.find( { metro: { $gte : { city: "New York" } } } );

// this query does not match the document because the order of fields is significant
db.factories.find( { metro: { state: "NY" , city: "New York" } } )

//

db.factories.ensureIndex( { "metro.city" : 1, "metro.state" : 1 } );
// these queries can use the above index:
db.factories.find( { "metro.city" : "New York", "metro.state" : "NY" } );
db.factories.find( { "metro.city" : "New York" } );
db.factories.find().sort( { "metro.city" : 1, "metro.state" : 1 } );
db.factories.find().sort( { "metro.city" : 1 } )



分组查询
> db.things.aggregate([ { $group:{_id:null,total:{$sum:1}}}]);
{ "result" : [ { "_id" : null, "total" : 24 } ], "ok" : 1 }

> db.things.aggregate([ { $group:{_id:null,total:{$sum:"$x"}}}]);
{ "result" : [ { "_id" : null, "total" : 24 } ], "ok" : 1 }

db.things.aggregate([ { $group:{_id:null,total:{$sum:"$j"}}}]);


SQL term	 	MongoDB agg framework term
WHERE	 		$match
GROUP BY	 	$group
SELECT	 		$project
ORDER BY	 	$sort

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
SELECT COUNT(*) FROM users
db.users.aggregate([ 
 { $group: {_id:null, count:{$sum:1}} }
])

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
SELECT SUM(price) FROM orders
db.orders.aggregate([ 
 { $group: {_id:null, 
            total:{$sum:"$price"} } }
])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
SELECT cust_id,SUM(price) FROM orders GROUP BY cust_id
db.orders.aggregate([ 
 { $group: {_id:"$cust_id",total:{$sum:"$price"}} }
])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
SELECT cust_id,SUM(price) FROM orders WHERE active=true GROUP BY cust_id
db.orders.aggregate([ 
 { $match:{active:true} }, 
 { $group:{_id:"$cust_id",total:{$sum:"$price"}} } 
])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

查询
> db.foo.insert( { x : 1, y : 1 } )
> db.foo.insert( { x : 2, y : "string" } )
> db.foo.insert( { x : 3, y : null } )
> db.foo.insert( { x : 4 } )

// Query #1documents where y has the value null or where y does not exist
> db.foo.find( { "y" : null } ) 
{ "_id" : ObjectId("4dc1975312c677fc83b5629f"), "x" : 3, "y" : null }
{ "_id" : ObjectId("4dc1975a12c677fc83b562a0"), "x" : 4 }

// Query #2documents where y has the value null　　？？？？
> db.foo.find( { "y" : { $type : 10 } } )
{ "_id" : ObjectId("4dc1975312c677fc83b5629f"), "x" : 3, "y" : null }

// Query #3	documents where y does not exist
> db.foo.find( { "y" : { $exists : false } } )
{ "_id" : ObjectId("4dc1975a12c677fc83b562a0"), "x" : 4 }



插入

{ author: 'joe',
  created : new Date('03/28/2009'),
  title : 'Yet another blog post',
  text : 'Here is the text...',
  tags : [ 'example', 'joe' ],
  comments : [ { author: 'jim', comment: 'I disagree' },
              { author: 'nancy', comment: 'Good post' }
  ]
}
> doc = { author: 'joe',created : new Date('03/28/2009'),title : 'Yet another blog post',text : 'Here is the text...',tags : [ 'example', 'joe' ],comments : [ { author: 'jim', comment: 'I disagree' },{ author: 'nancy', comment: 'Good post' }]}
> db.posts.insert(doc);
> db.posts.find( { "comments.author" : "jim" } )

更新

> db.mycollection.save(x); // updates if exists; inserts if new> // equivalent to:
> db.mycollection.update( { _id: x._id }, x, /*upsert*/ true );

db.people.update( { name:"Joe" }, { $inc: { n : 1 } } );
//{ $set : { x : 1 , y : 2 } } { $set : { x : 1 }, $inc : { y : 1 } }


{ $unset : { field : 1} } eletes a given field.
http://www.mongodb.org/display/DOCS/Updating



删除

db.things.remove({});    // removes all
db.things.remove({n:1}); // removes all where n == 1

手册http://docs.mongodb.org/manual/

setup.py内容

import glob
import os
import subprocess
import sys
import warnings

# Hack to silence atexit traceback in newer python versions.
try:
    import multiprocessing
except ImportError:
    pass

try:
    from ConfigParser import SafeConfigParser
except ImportError:
    # PY3
    from configparser import SafeConfigParser

# Don't force people to install distribute unless
# we have to.
try:
    from setuptools import setup, Feature
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, Feature

from distutils.cmd import Command
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError
from distutils.errors import DistutilsPlatformError, DistutilsExecError
from distutils.core import Extension

version = "2.3+"

f = open("README.rst")
try:
    try:
        readme_content = f.read()
    except:
        readme_content = ""
finally:
    f.close()

PY3 = sys.version_info[0] == 3

nose_config_options = {
    'with-xunit': '1',    # Write out nosetests.xml for CI.
    'py3where': 'build',  # Tell nose where to find tests under PY3.
}

def write_nose_config():
    """Write out setup.cfg. Since py3where has to be set
    for tests to run correctly in Python 3 we create this
    on the fly.
    """
    config = SafeConfigParser()
    config.add_section('nosetests')
    for opt, val in nose_config_options.items():
        config.set('nosetests', opt, val)
    try:
        cf = open('setup.cfg', 'w')
        config.write(cf)
    finally:
        cf.close()


def should_run_tests():
    if "test" in sys.argv or "nosetests" in sys.argv:
        return True
    return False


class doc(Command):

    description = "generate or test documentation"

    user_options = [("test", "t",
                     "run doctests instead of generating documentation")]

    boolean_options = ["test"]

    def initialize_options(self):
        self.test = False

    def finalize_options(self):
        pass

    def run(self):
        if self.test:
            path = "doc/_build/doctest"
            mode = "doctest"
        else:
            path = "doc/_build/%s" % version
            mode = "html"

            try:
                os.makedirs(path)
            except:
                pass

        status = subprocess.call(["sphinx-build", "-E",
                                  "-b", mode, "doc", path])

        if status:
            raise RuntimeError("documentation step '%s' failed" % (mode,))

        sys.stdout.write("\nDocumentation step '%s' performed, results here:\n"
                         "   %s/\n" % (mode, path))


if sys.platform == 'win32' and sys.version_info > (2, 6):
    # 2.6's distutils.msvc9compiler can raise an IOError when failing to
    # find the compiler
    build_errors = (CCompilerError, DistutilsExecError,
                    DistutilsPlatformError, IOError)
else:
    build_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError)


class custom_build_ext(build_ext):
    """Allow C extension building to fail.

    The C extension speeds up BSON encoding, but is not essential.
    """

    warning_message = """
********************************************************************
WARNING: %s could not
be compiled. No C extensions are essential for PyMongo to run,
although they do result in significant speed improvements.
%s

Please see the installation docs for solutions to build issues:

http://api.mongodb.org/python/current/installation.html

Here are some hints for popular operating systems:

If you are seeing this message on Linux you probably need to
install GCC and/or the Python development package for your
version of Python.

Debian and Ubuntu users should issue the following command:

    $ sudo apt-get install build-essential python-dev

RedHat, CentOS, and Fedora users should issue the following command:

    $ sudo yum install gcc python-devel

If you are seeing this message on Microsoft Windows please install
PyMongo using the MS Windows installer for your version of Python,
available on pypi here:

http://pypi.python.org/pypi/pymongo/#downloads

If you are seeing this message on OSX please read the documentation
here:

http://api.mongodb.org/python/current/installation.html#osx
********************************************************************
"""

    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError:
            e = sys.exc_info()[1]
            sys.stdout.write('%s\n' % str(e))
            warnings.warn(self.warning_message % ("Extension modules",
                                                  "There was an issue with "
                                                  "your platform configuration"
                                                  " - see above."))

    def set_nose_options(self):
        # Under python 3 we need to tell nose where to find the
        # proper tests. if we built the C extensions this will be
        # someplace like build/lib.<os>-<arch>-<python version>
        if PY3:
            ver = '.'.join(map(str, sys.version_info[:2]))
            lib_dirs = glob.glob(os.path.join('build', 'lib*' + ver))
            if lib_dirs:
                nose_config_options['py3where'] = lib_dirs[0]
        write_nose_config()

    def build_extension(self, ext):
        name = ext.name
        if sys.version_info[:3] >= (2, 4, 0):
            try:
                build_ext.build_extension(self, ext)
                if should_run_tests():
                    self.set_nose_options()
            except build_errors:
                e = sys.exc_info()[1]
                sys.stdout.write('%s\n' % str(e))
                warnings.warn(self.warning_message % ("The %s extension "
                                                      "module" % (name,),
                                                      "The output above "
                                                      "this warning shows how "
                                                      "the compilation "
                                                      "failed."))
        else:
            warnings.warn(self.warning_message % ("The %s extension "
                                                  "module" % (name,),
                                                  "Please use Python >= 2.4 "
                                                  "to take advantage of the "
                                                  "extension."))

c_ext = Feature(
    "optional C extensions",
    standard=True,
    ext_modules=[Extension('bson._cbson',
                           include_dirs=['bson'],
                           sources=['bson/_cbsonmodule.c',
                                    'bson/time64.c',
                                    'bson/buffer.c',
                                    'bson/encoding_helpers.c']),
                 Extension('pymongo._cmessage',
                           include_dirs=['bson'],
                           sources=['pymongo/_cmessagemodule.c',
                                    'bson/buffer.c'])])

if "--no_ext" in sys.argv:
    sys.argv = [x for x in sys.argv if x != "--no_ext"]
    features = {}
elif (sys.platform.startswith("java") or
      sys.platform == "cli" or
      "PyPy" in sys.version):
    sys.stdout.write("""
*****************************************************\n
The optional C extensions are currently not supported\n
by this python implementation.\n
*****************************************************\n
""")
    features = {}
elif sys.byteorder == "big":
    sys.stdout.write("""
*****************************************************\n
The optional C extensions are currently not supported\n
on big endian platforms and will not be built.\n
Performance may be degraded.\n
*****************************************************\n
""")
    features = {}
else:
    features = {"c-ext": c_ext}

extra_opts = {
    "packages": ["bson", "pymongo", "gridfs"],
    "test_suite": "nose.collector"
}
if PY3:
    extra_opts["use_2to3"] = True
    if should_run_tests():
        # Distribute isn't smart enough to copy the
        # tests and run 2to3 on them. We don't want to
        # install the test suite so only do this if we
        # are testing.
        # https://bitbucket.org/tarek/distribute/issue/233
        extra_opts["packages"].append("test")
        # Hack to make "python3.x setup.py nosetests" work in python 3
        # otherwise it won't run 2to3 before running the tests.
        if "nosetests" in sys.argv:
            sys.argv.remove("nosetests")
            sys.argv.append("test")
            # All "nosetests" does is import and run nose.main.
            extra_opts["test_suite"] = "nose.main"

# This may be called a second time if
# we are testing with C extensions.
if should_run_tests():
    write_nose_config()

setup(
    name="pymongo",
    version=version,
    description="Python driver for MongoDB <http://www.mongodb.org>",
    long_description=readme_content,
    author="Mike Dirolf",
    author_email="mongodb-user@googlegroups.com",
    maintainer="Bernie Hackett",
    maintainer_email="bernie@10gen.com",
    url="http://github.com/mongodb/mongo-python-driver",
    keywords=["mongo", "mongodb", "pymongo", "gridfs", "bson"],
    install_requires=[],
    features=features,
    license="Apache License, Version 2.0",
    tests_require=["nose"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Database"],
    cmdclass={"build_ext": custom_build_ext,
              "doc": doc},
    **extra_opts
)
