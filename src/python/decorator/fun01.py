'''
Created on 2012-10-22

@author: wangliang
'''
def deco_functionNeedDoc(func):
    if func.__doc__ == None :
        print func.__name__,"() has no Document, it's a bad habit."
    else:
        print func.__name__,'() Doc:', func.__doc__, '.'
    return func
@deco_functionNeedDoc
def f():
    print 'f() Do something'
    
    
@deco_functionNeedDoc
def g():
    'I have a __doc__ Comment...'
    print 'g() Do something'
f()
g()

def a1(x):
    print 'a1 Do something',x
    return x
 
@a1
def b1():
    print "hello",10
     
b1()


def a2(x):
    def a22():
        print x()+30
    return a22
 
@a2
def b2():
    return 20
     
b2()

def a3(x):
    return lambda : x()+50
 
@a3
def b3():    
    return 40
     
print b3()

#http://jnotes.googlecode.com/svn/trunk/Notes/NotesOnPythonLearning/Python_decorator.html
#http://bu-choreography.iteye.com/blog/1236881