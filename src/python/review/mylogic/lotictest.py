#coding:utf-8
test1 = 12
test2 = 0
test3 = ''
test4 = "First"
print test1 and test3   #result = ''
print test3 and test1   #result = ''
print test1 and test4   #result = "First"
print test4 and test1   #result = 12
print test1 or test2    #result = 12
print test1 or test3    #result = 12
print test3 or test4    #result = "First"
print test2 or test4    #result = "First"
print test1 or test4    #result = 12
print test4 or test1    #result = "First"
print test2 or test3    #result = ''
print test3 or test2    #result = 0

#Python的逻辑操作有三种：and、or、not。分别对应与、或、非。
#在Python中，空字符串为假，非空字符串为真。非零的数为真。
#对于and操作符：
#    只要左边的表达式为真，整个表达式返回的值是右边表达式的值，否则，返回左边表达式的值
#对于or操作符：
#    两边的表达式为真，结果是左边表达式的值。
#    如果是一真一假，返回真值表达式的值
#    如果两个都是假，比如空值和0，返回的是右边的值。（空值或0）
    
    
    
    