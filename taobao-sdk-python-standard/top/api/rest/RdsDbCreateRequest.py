'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class RdsDbCreateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.db_name = None
		self.instance_name = None

	def getapiname(self):
		return 'taobao.rds.db.create'
