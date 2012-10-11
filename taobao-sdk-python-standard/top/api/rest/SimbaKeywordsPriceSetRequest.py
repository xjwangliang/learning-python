'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaKeywordsPriceSetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.keywordid_prices = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.keywords.price.set'
