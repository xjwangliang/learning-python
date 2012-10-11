'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class UserrecommendItemsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.recommend_type = None

	def getapiname(self):
		return 'taobao.userrecommend.items.get'
