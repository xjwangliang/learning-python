'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaRptAdgroupcreativebaseGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.campaign_id = None
		self.end_time = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.search_type = None
		self.source = None
		self.start_time = None
		self.subway_token = None

	def getapiname(self):
		return 'taobao.simba.rpt.adgroupcreativebase.get'
