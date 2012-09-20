>>> 7*(7+2,)

>>x=["abc","dd","uyyyy","78",33]  
>>x.sort(key=len,reverse=True) # TypeError: object of type 'int' has no len()


>>x=["abc","dd","uyyyy","78","wang"]
>>x.sort(key=len,reverse=True)




comp(x,y)
max(args)
min(args)

list(seq)
len(seq)

sorted(seq)
reversed(seq)
tuple(seq)			//tuple([1,2,3])  tuple('abc')




字符串方法
title = "my name is wangliang"
title.find("name")
title.find("li")	title.find("li",8,9)
title.count("i")
title.index("nam")
title.startswith("na")	endswith


dirs = "","usr","bin","local"
"\\".join(dirs)				＃'\\usr\\bin\\local'
print "\\".join(dirs) 		#打印\usr\bin\local
print 'C:'+'\\'.join(dirs)
jj = "/".join(dirs)
jj.split('/')				#['', 'usr', 'bin', 'local']
jj2 = "\\".join(dirs)
jj2.split('\\')				#['', 'usr', 'bin', 'local']


title = '&*!!!   *& my name is wangliang*** \\*&*'
title.strip('*')			
title.strip('*&! \\')		#去除首尾字符：'my name is wangliang'；原始数据不变





lower()
replace()
split()
strip()





