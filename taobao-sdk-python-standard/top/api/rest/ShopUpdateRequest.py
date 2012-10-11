'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class ShopUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.bulletin = None
		self.desc = None
		self.title = None

	def getapiname(self):
		return 'taobao.shop.update'
