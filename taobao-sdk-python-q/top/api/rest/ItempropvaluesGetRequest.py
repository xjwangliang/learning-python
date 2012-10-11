'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class ItempropvaluesGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.fields = None
		self.pvs = None
		self.type = None

	def getapiname(self):
		return 'taobao.itempropvalues.get'
