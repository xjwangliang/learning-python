'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaAdgroupsItemExistRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.item_id = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.adgroups.item.exist'
