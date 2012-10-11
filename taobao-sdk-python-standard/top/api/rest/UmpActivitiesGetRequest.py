'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class UmpActivitiesGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.tool_id = None

	def getapiname(self):
		return 'taobao.ump.activities.get'
