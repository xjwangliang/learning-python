#encoding=utf-8
'''
Created on 2012-10-22

@author: wangliang
'''
def logfunc(func):
    
    def wrapper():
        print "Function %s() called" % func.__name__
#        return func()
    return wrapper


@logfunc
def foo():
    print "Inside function foo"
  
logfunc(foo)
print "-----------logFunc(foo)()-----------\n"  
logfunc(foo)()
print "---------foo()-------------\n"
foo()
print "---------logFunc(foo)()-------------\n"
d = logfunc(foo)
d()

#----------------------
#
#Function wrappedFunc() called
#Function foo() called
#Inside function foo
#----------------------
#
#Function foo() called
#Inside function foo