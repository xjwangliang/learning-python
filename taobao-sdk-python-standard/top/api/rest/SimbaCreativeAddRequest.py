'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaCreativeAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.img_url = None
		self.nick = None
		self.title = None

	def getapiname(self):
		return 'taobao.simba.creative.add'
