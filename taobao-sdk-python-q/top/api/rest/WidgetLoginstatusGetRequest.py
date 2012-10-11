'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class WidgetLoginstatusGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.nick = None

	def getapiname(self):
		return 'taobao.widget.loginstatus.get'
