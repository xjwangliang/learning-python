'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class LogisticsTraceSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.seller_nick = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.trace.search'
