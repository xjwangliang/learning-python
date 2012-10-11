'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbItemConsignmentCreateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.number = None
		self.owner_item_id = None
		self.owner_user_id = None
		self.rule_id = None

	def getapiname(self):
		return 'taobao.wlb.item.consignment.create'
