#encoding=utf-8
'''
Created on 2012-10-22

@author: wangliang
'''

import time
 
 
# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        print "Function %s() called" % func.__name__
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start," in function ",func.__name__
     
    # 将包装后的函数返回
    return wrapper

def foo1():
    print 'in foo1()'
    
@timeit
def foo2():
    print 'in foo2()'
print "\n----timeit(foo1)()------"
timeit(foo1)()

print "\n----timeit(foo2)------"
timeit(foo2)

print "\n-----timeit(foo2)()------"    
timeit(foo2)()
#foo2相当于wrapper，那么timeit(foo2)得到wrapper(参数)，timeit(foo2)()为wrapper()相当于执行
#def wrapper():
#        print "Function %s() called" % wrapper.__name__
#        start = time.clock()
#        #wrapper()相当于下面

#        print "Function %s() called" % foo2.__name__
#        start = time.clock()
#        foo2()
#        end =time.clock()
#        print 'used:', end - start," in function ",foo2.__name__

#        end =time.clock()
#        print 'used:', end - start," in function ",wrapper.__name__

print "\n----foo2()-------"
foo2()
#注意timeit(foo2)()和foo2()并不相同，没有加上@timeit，timeit(foo2)()才与加上了@timeit的foo2()相同


print "\n----foo2.name-------"
print foo2.__name__

