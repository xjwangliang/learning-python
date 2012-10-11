'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaToolsItemsTopGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.ip = None
		self.keyword = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.tools.items.top.get'
