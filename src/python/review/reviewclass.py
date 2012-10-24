#encoding=utf-8
from django.conf.locale import en
class BookPhoneEntry(object):
    #类变量
    version = 1.0
    
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        
        
    def update_phone(self,phone):
        self.phone = phone
        




    
print BookPhoneEntry.version    #BookPhoneEntry.name出错

BookPhoneEntry.int_version = 10 #动态添加类属性
print BookPhoneEntry.int_version

entry = BookPhoneEntry("wangliang",1245)
print entry.name,entry.phone

entry.update_phone("dddd")
print entry.name,entry.phone



class EmpleeBookPhoneEntry(BookPhoneEntry):
    def __init__(self,name,phone,grade,emp_id):
        BookPhoneEntry.__init__(self, name, phone)
        self.emp_id = emp_id ;
        self.grade = grade 


print EmpleeBookPhoneEntry.version      #1.0   
print EmpleeBookPhoneEntry.version      #1.0    
EmpleeBookPhoneEntry.version = 9.0
print BookPhoneEntry.version            #1.0
print EmpleeBookPhoneEntry.version      #9.0


print EmpleeBookPhoneEntry.int_version  #10
print BookPhoneEntry.int_version        #10
BookPhoneEntry.int_version = 20 #动态添加类属性
print EmpleeBookPhoneEntry.int_version  #20
print BookPhoneEntry.int_version        #20


empEntry = EmpleeBookPhoneEntry("Han", 12345678, 1, 9000)
print empEntry.name,empEntry.phone,empEntry.grade

empEntry.update_phone(888888)
print empEntry.name,empEntry.phone,empEntry.grade

#嵌套类


