'''
Created on 2012-9-20

@author: wangliang
'''

def testif():
    print 'hello world'
    name = raw_input("Your name is ?")
    if name.startswith("w"):
        print 'Success'
    else:
        print'Error'
        
        
def testOperation():
    y = ['wang','linag','han']
    x = 'song'
    x2 = 'song'
    x3 = "song"
    print 'x == x2 ? %s' % bool(x == x2)    #x == x2 ? True
    print 'x == x3 ? %s' % bool(x == x3)    #x == x3 ? True
    print 'x is x3 ? %s' % (x is x2)        #x is x3 ? True
    
    y2 = ['wang','linag','han']
    print 'y == y2 ? %s' % bool( y== y2)    #y == y2 ? True
    print 'y is y ? %s' % (y is y2)         #y is y ? False
    
    if x in y:
        print '%s in y' % x
    else:
        print '%s not in y' % x
        
    print '%s not in string %s ? %s' % ('a','abc',('bc' in 'abc'))  #a not in string abc ? True
    
if __name__ == '__main__':
    testOperation()