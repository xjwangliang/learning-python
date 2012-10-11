'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class JipiaoPolicystatusUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.policy_id = None
		self.status = None
		self.type = None

	def getapiname(self):
		return 'taobao.jipiao.policystatus.update'
