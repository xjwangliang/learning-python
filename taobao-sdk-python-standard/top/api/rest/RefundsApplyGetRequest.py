'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class RefundsApplyGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.seller_nick = None
		self.status = None
		self.type = None

	def getapiname(self):
		return 'taobao.refunds.apply.get'
