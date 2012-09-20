# encoding=utf-8
# hello4.py
def hello():
    print "Hello, world!"

def test():
    hello()

if __name__ == '__main__': test()

#在你写的这段程序中如果以主程序运行的话　__name__ 参数就等于 __main__ 
#

#有的时候写的类。模块，库，都有这段代码，如果单独运行的话，可以进行个简单的测试。如果是其他程序IMPORT的话，就不会运行
#if   __name__  ==  "__main__":
#      
#       main()
#
#中间的代码。

