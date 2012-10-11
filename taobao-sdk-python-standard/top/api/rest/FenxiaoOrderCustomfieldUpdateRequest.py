'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoOrderCustomfieldUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.isv_custom_key = None
		self.isv_custom_value = None
		self.purchase_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.order.customfield.update'
