'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class RefundRefuseRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.refund_id = None
		self.refuse_message = None
		self.refuse_proof = None
		self.tid = None

	def getapiname(self):
		return 'taobao.refund.refuse'
