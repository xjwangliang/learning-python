'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class IncrementCustomerPermitRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.status = None
		self.topics = None
		self.type = None

	def getapiname(self):
		return 'taobao.increment.customer.permit'
