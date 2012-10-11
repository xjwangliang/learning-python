'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TaobaokeWidgetUrlConvertRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.outer_code = None
		self.url = None

	def getapiname(self):
		return 'taobao.taobaoke.widget.url.convert'
