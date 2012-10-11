'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderFindRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.begin_time = None
		self.end_time = None
		self.page = None
		self.policy_id = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.find'
