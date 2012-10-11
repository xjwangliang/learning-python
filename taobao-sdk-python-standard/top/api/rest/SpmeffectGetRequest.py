'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SpmeffectGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.date = None
		self.module_detail = None
		self.page_detail = None

	def getapiname(self):
		return 'taobao.spmeffect.get'
