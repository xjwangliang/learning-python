'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class UmpPromotionGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.channel_key = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.ump.promotion.get'
