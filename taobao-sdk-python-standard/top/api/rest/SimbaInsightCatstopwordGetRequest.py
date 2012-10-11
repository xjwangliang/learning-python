'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaInsightCatstopwordGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.category_ids = None
		self.nick = None
		self.result_num = None

	def getapiname(self):
		return 'taobao.simba.insight.catstopword.get'
