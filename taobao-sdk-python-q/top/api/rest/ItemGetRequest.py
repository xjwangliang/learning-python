'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class ItemGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.num_iid = None
		self.track_iid = None

	def getapiname(self):
		return 'taobao.item.get'
