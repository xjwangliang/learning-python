'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class LogisticsOnlineConfirmRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.out_sid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.online.confirm'
