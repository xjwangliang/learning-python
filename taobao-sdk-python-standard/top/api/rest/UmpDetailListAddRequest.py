'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class UmpDetailListAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.details = None

	def getapiname(self):
		return 'taobao.ump.detail.list.add'
