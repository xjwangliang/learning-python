'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaAdgroupCatmatchUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.catmatch_id = None
		self.max_price = None
		self.nick = None
		self.online_status = None
		self.use_default_price = None

	def getapiname(self):
		return 'taobao.simba.adgroup.catmatch.update'
