'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class ItemSkusGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.num_iids = None

	def getapiname(self):
		return 'taobao.item.skus.get'
