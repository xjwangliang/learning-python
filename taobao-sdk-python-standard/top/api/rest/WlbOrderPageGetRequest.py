'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbOrderPageGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.order_code = None
		self.order_status = None
		self.order_sub_type = None
		self.order_type = None
		self.page_no = None
		self.page_size = None
		self.start_time = None

	def getapiname(self):
		return 'taobao.wlb.order.page.get'
