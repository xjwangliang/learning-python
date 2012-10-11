'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class HotelSoldOrdersIncrementGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.need_guest = None
		self.need_message = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.status = None
		self.use_has_next = None

	def getapiname(self):
		return 'taobao.hotel.sold.orders.increment.get'
