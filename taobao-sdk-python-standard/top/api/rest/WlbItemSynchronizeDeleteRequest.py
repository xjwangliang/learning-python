'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbItemSynchronizeDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.ext_entity_id = None
		self.ext_entity_type = None
		self.item_id = None

	def getapiname(self):
		return 'taobao.wlb.item.synchronize.delete'
