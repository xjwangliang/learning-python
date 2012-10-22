#encoding=utf-8
'''
Created on 2012-10-22

@author: wangliang
'''
import os  
a=os.walk(r'/Users/wangliang/Documents/Aptana Studio 3 Workspace/Python-Fundmental/src/') 
for f in a:
    pass
#    print f

#def decomaker(arg):
#    '通常对arg会有一定的要求'
#    """由于有参数的decorator函数在调用时只会使用应用时的参数
#       而不接收被装饰的函数做为参数，所以必须在其内部再创建
#       一个函数
#    """
#    def newDeco(func):    #定义一个新的decorator函数
#        print func, arg
#        return func
#    return newDeco
#
#@decomaker(deco_args)
#def foo():pass
#foo()

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello world"
 


@makebold
@makeitalic
def say():
    return "Hello"

print hello() ## 返回 <b><i>hello world</i></b>