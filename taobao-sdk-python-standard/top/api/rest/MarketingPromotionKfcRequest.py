'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class MarketingPromotionKfcRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.promotion_desc = None
		self.promotion_title = None

	def getapiname(self):
		return 'taobao.marketing.promotion.kfc'
