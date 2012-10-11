'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class AlipayTopatsUserAccountreportGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.end_time = None
		self.fields = None
		self.start_time = None
		self.type = None

	def getapiname(self):
		return 'alipay.topats.user.accountreport.get'
