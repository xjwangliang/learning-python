'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoCooperationUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.distributor_id = None
		self.grade_id = None
		self.trade_type = None

	def getapiname(self):
		return 'taobao.fenxiao.cooperation.update'
