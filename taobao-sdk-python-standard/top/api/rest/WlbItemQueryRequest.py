'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbItemQueryRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.is_sku = None
		self.item_code = None
		self.item_type = None
		self.name = None
		self.page_no = None
		self.page_size = None
		self.parent_id = None
		self.status = None
		self.title = None

	def getapiname(self):
		return 'taobao.wlb.item.query'
