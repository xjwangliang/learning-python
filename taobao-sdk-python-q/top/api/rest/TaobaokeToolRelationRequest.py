'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class TaobaokeToolRelationRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.pubid = None

	def getapiname(self):
		return 'taobao.taobaoke.tool.relation'
