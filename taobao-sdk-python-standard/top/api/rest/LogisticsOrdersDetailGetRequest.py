'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class LogisticsOrdersDetailGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.end_created = None
		self.fields = None
		self.freight_payer = None
		self.page_no = None
		self.page_size = None
		self.receiver_name = None
		self.seller_confirm = None
		self.start_created = None
		self.status = None
		self.tid = None
		self.type = None

	def getapiname(self):
		return 'taobao.logistics.orders.detail.get'
