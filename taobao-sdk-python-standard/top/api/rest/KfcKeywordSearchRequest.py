'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class KfcKeywordSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.apply = None
		self.content = None
		self.nick = None

	def getapiname(self):
		return 'taobao.kfc.keyword.search'
