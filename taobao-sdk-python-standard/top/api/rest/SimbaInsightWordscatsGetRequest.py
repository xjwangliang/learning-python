'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaInsightWordscatsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.filter = None
		self.nick = None
		self.word_categories = None

	def getapiname(self):
		return 'taobao.simba.insight.wordscats.get'
