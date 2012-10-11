'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class PromotionLimitdiscountGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.limit_discount_id = None
		self.page_number = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'taobao.promotion.limitdiscount.get'
