'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class JipiaoAgentorderFailRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.memo = None
		self.order_id = None
		self.reason = None

	def getapiname(self):
		return 'taobao.jipiao.agentorder.fail'
