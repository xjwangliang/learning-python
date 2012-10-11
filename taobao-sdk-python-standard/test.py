'''
Created on 2012-7-3

@author: lihao
'''
import top.api as topapi
import top

a = topapi.TaobaoUserGetRequest("api.daily.taobao.net",80)
a.set_app_info(top.appinfo("your appkey","your secret"))
a.name = "not need para"
a.nick = "tbtest561"


try:
    f= a.getResponse()
    print(f)
except Exception,e:
    print(e)
    
