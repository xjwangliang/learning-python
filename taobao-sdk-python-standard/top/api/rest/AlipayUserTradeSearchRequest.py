'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class AlipayUserTradeSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.alipay_order_no = None
		self.end_time = None
		self.merchant_order_no = None
		self.order_from = None
		self.order_status = None
		self.order_type = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'alipay.user.trade.search'
