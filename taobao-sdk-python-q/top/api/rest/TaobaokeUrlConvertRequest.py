'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class TaobaokeUrlConvertRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.outer_code = None
		self.url = None

	def getapiname(self):
		return 'taobao.taobaoke.url.convert'
