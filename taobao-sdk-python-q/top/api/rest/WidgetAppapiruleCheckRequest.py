'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class WidgetAppapiruleCheckRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.api_name = None

	def getapiname(self):
		return 'taobao.widget.appapirule.check'
