'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbItemCombinationCreateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.dest_item_list = None
		self.item_id = None
		self.proportion_list = None

	def getapiname(self):
		return 'taobao.wlb.item.combination.create'