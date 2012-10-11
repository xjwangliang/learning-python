'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TradeCloseRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.close_reason = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.close'
