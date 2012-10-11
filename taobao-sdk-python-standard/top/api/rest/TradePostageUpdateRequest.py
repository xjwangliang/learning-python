'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TradePostageUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.post_fee = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.postage.update'
