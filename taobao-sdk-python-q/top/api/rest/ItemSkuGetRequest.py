'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class ItemSkuGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.nick = None
		self.num_iid = None
		self.sku_id = None

	def getapiname(self):
		return 'taobao.item.sku.get'
