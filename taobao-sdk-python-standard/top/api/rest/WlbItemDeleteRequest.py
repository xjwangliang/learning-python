'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbItemDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.wlb.item.delete'
