'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaRptCustbaseGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.source = None
		self.start_time = None
		self.subway_token = None

	def getapiname(self):
		return 'taobao.simba.rpt.custbase.get'
