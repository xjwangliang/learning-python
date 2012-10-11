'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TradeOrderskuUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.sku_id = None
		self.sku_props = None

	def getapiname(self):
		return 'taobao.trade.ordersku.update'
