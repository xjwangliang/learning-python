创建字典
d = dict([('name',"wangliang"),("age",24)])
d2 = dict("name" ="wangliang","age" = 24)		##SyntaxError: keyword can't be an expression
d2 = dict(name ="wangliang",age = 24)

操作　len(dict)/dict[key]/del dict[key]/key in dict

方法 

dict.clear()(返回空的dict)　字典赋值是引用，操作是对原始的字典起作用，但是赋值操作不会，例如
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
x = {}
y = x 
y['key'] = "value"

y= {}		#此时x与y不同，为{'key': 'value'}
y = x		#此时y和x相同
y.clear()	#此时y和x相同，为{}

clear和list的sort都是原地操作
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

copy　浅拷贝
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
origin = {"name":"wangliang","machines":["abc","def","hello"]}
c = origin.copy()
c["name"] = 'Han'					#origin不变，c变化（替换操作）
c["machines"].append("world")		#origin和c都变化（原地修改操作）
c["machines"].remove("world")		#origin和c都变化

deepcopy　浅拷贝　from copy import deepcopy重复上面的代码，拷贝值和原始值没有关系
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

fromkeys
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {"name":"wanliang"}
d.fromkeys(["name","age"])				#{'age': None, 'name': None}
d.fromkeys(["name","age"],"unkown")		#{'age': 'unkown', 'name': 'unkown'}
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

get
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {"name":"wanliang"}
d['names']				#出错
print d.get("names")	#None
print d.get("names","not exists")	#None
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


has_key()
items()
iteritems()
keys()
iterkeys()
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {"name":"wanliang"}
d.items()
list(d.iteritems())

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

pop(key)返回值,不存在则出错
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {"name":"wanliang"}
dd = d
d.pop("name") # d 和　dd都是{}
			
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

popitem()随机弹出一个,与list的pop不同
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {"name":"wanliang","age":24}
d.popitem()
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

setdefault(key [,value])
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {'age': 24, 'name': 'wanliang'}
d.setdefault("name","UN")		#不变
d.setdefault("gender","UN")		#{'gender': 'UN', 'age': 24, 'name': 'wanliang'}
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


update(dict)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {'age': 24, 'name': 'wanliang'}
n = {'name': 'Han',"gender":"male"}
d.update(n)											#{'gender': 'male', 'age': 24, 'name': 'Han'}
d.update([('name',"wangliang"),("age2",24)])		#{'gender': 'male', 'age': 24, 'name': 'wangliang', 'age2': 24}
d.update(name ="Han",age = 20,ok = True)			#{'ok': True, 'name': 'Han', 'gender': 'male', 'age': 20, 'age2': 24}
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

keys() values() itervalues
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = {}
d[0] = 1 ;
d[1] = 2 ;
d[2] = 3 ;
#{0: 1, 1: 2, 2: 3}


format = "My name is %s ,age is %d ;In math pi is %.20f"		#len.presition是右对齐的；-是左对齐的
from math import pi
values = ("wangliang",24,pi)
print format % values

格式化

格式化的妙用
phonebook = {"wang":'1234',"Tang":'788778',"Han":'1289'}
'Wang\'s phone number is %(wang)s' % phonebook


template = '''<html>
	<head>
		<title>%(title)s</title>
	</head>
	<body>
	%(body)s
	</body>
</html>'''

data = {"title":"hello　world","body":"content"}
template % data				##换行符用\n表示
print template % data		##并不会改变template




区别
>>> print 'hello'+',' ,'world'	#hello, world
>>> print 'hello',',' ,'world'	#hello , world
