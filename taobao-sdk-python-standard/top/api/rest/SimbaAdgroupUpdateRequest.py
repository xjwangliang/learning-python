'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaAdgroupUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.default_price = None
		self.nick = None
		self.nonsearch_max_price = None
		self.online_status = None
		self.use_nonsearch_default_price = None

	def getapiname(self):
		return 'taobao.simba.adgroup.update'
