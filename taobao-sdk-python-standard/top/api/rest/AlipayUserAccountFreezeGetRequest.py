'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class AlipayUserAccountFreezeGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.freeze_type = None

	def getapiname(self):
		return 'alipay.user.account.freeze.get'
