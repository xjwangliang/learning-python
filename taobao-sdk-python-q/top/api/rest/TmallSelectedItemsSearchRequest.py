'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class TmallSelectedItemsSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cid = None

	def getapiname(self):
		return 'tmall.selected.items.search'
