'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoOrderMessageAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.message = None
		self.purchase_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.order.message.add'
