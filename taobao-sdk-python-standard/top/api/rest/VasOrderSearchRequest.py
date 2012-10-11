'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class VasOrderSearchRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.article_code = None
		self.biz_order_id = None
		self.biz_type = None
		self.end_created = None
		self.item_code = None
		self.nick = None
		self.order_id = None
		self.page_no = None
		self.page_size = None
		self.start_created = None

	def getapiname(self):
		return 'taobao.vas.order.search'
