'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WangwangEserviceReceivenumGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.service_staff_id = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.receivenum.get'
