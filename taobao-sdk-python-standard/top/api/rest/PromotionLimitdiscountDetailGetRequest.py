'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class PromotionLimitdiscountDetailGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.limit_discount_id = None

	def getapiname(self):
		return 'taobao.promotion.limitdiscount.detail.get'
