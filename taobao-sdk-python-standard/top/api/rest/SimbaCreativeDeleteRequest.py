'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaCreativeDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.creative_id = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.creative.delete'
