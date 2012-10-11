'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TopatsTradesSoldGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.fields = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.topats.trades.sold.get'
