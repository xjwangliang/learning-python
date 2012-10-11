'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class ItemcatsIncrementGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cids = None
		self.days = None
		self.type = None

	def getapiname(self):
		return 'taobao.itemcats.increment.get'
