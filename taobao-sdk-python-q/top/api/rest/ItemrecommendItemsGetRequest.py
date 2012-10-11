'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class ItemrecommendItemsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.item_id = None
		self.recommend_type = None

	def getapiname(self):
		return 'taobao.itemrecommend.items.get'
