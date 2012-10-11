'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaKeywordsRecommendGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.nick = None
		self.order_by = None
		self.page_no = None
		self.page_size = None
		self.pertinence = None
		self.search = None

	def getapiname(self):
		return 'taobao.simba.keywords.recommend.get'
