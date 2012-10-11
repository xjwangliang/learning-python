'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class TimeGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.time.get'
