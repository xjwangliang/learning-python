'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class LogisticsOfflineSendRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cancel_id = None
		self.company_code = None
		self.feature = None
		self.out_sid = None
		self.sender_id = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.offline.send'
