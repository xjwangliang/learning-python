'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaAdgroupAdgroupcatmatchsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_ids = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.adgroup.adgroupcatmatchs.get'
