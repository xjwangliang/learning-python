'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderFailRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fail_memo = None
		self.fail_type = None
		self.order_id = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.fail'
