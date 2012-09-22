# encoding=utf-8
'''
Created on 2012-9-22

@author: wangliang
'''

from urllib import urlopen, urlretrieve, urlcleanup
import re
from _pyio import open

webapp = urlopen("http://www.baidu.com")
print webapp.read()

file = open("hello.txt")
p = r'/Users/wangliang/Documents/Aptana Studio 3 Workspace/Python-Fundmental/src/python/Chapter14/hello.txt' #空格没有关心
data = urlretrieve('http://www.baidu.com', p)
print data
urlcleanup()