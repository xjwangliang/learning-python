'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TradeConfirmfeeGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.is_detail = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.confirmfee.get'
