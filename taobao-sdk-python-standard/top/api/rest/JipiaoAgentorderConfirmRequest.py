'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class JipiaoAgentorderConfirmRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.latest_ticket_time = None
		self.order_id = None

	def getapiname(self):
		return 'taobao.jipiao.agentorder.confirm'
