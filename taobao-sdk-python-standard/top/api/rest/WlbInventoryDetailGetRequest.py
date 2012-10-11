'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbInventoryDetailGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.inventory_type_list = None
		self.item_id = None
		self.store_code = None

	def getapiname(self):
		return 'taobao.wlb.inventory.detail.get'
