'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class UmpToolAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.content = None

	def getapiname(self):
		return 'taobao.ump.tool.add'
