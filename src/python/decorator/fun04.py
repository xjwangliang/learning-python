#encoding=utf-8
import time
import functools
 
def timeit(func):
    @functools.wraps(func)
    def wrapper():
        print "Called in function ",func.__name__
        
        start = time.clock()
        func()
        end =time.clock()
        print "used ", end - start," in function ",func.__name__
    return wrapper
 
@timeit
def foo():
    print 'in foo()'
 
foo()
print "foo name is ",foo.__name__
timeit(foo)()
#注意上面这一句timeit(foo)()的执行结果为
#Called in function  foo
#Called in function  foo
#in foo()
#used  2e-06  in function  foo
#used  1.7e-05  in function  foo


#首先注意第5行，如果注释这一行，foo.__name__将是'wrapper'。另外相信你也注意到了，这个装饰器竟然带有一个参数。实际上，他还有另外两个可选的参数，
#assigned中的属性名将使用赋值的方式替换，而updated中的属性名将使用update的方式合并，你可以通过查看functools的源代码获得它们的默认值。对于这个装饰器，\
#相当于wrapper = functools.wraps(func)(wrapper)。


#http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html