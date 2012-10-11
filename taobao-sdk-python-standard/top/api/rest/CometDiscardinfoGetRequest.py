'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class CometDiscardinfoGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end = None
		self.nick = None
		self.start = None
		self.types = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.comet.discardinfo.get'
