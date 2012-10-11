'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class AlipayUserGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.auth_token = None
		self.fields = None

	def getapiname(self):
		return 'alipay.user.get'
