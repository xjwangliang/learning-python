'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbItemConsignmentPageGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.ic_item_id = None
		self.owner_item_id = None
		self.owner_user_nick = None

	def getapiname(self):
		return 'taobao.wlb.item.consignment.page.get'
