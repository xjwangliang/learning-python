'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class AlipaySystemOauthTokenRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.code = None
		self.grant_type = None
		self.refresh_token = None

	def getapiname(self):
		return 'alipay.system.oauth.token'
