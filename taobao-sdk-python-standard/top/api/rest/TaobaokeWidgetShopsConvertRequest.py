'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class TaobaokeWidgetShopsConvertRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.is_mobile = None
		self.outer_code = None
		self.seller_nicks = None

	def getapiname(self):
		return 'taobao.taobaoke.widget.shops.convert'
