'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class RefundsReceiveGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.end_modified = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.status = None
		self.type = None

	def getapiname(self):
		return 'taobao.refunds.receive.get'
