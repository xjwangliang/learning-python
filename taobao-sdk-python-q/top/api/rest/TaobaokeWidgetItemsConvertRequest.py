'''
Created by auto_sdk on 2012-09-23 16:40:21
'''
from top.api.base import RestApi
class TaobaokeWidgetItemsConvertRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.is_mobile = None
		self.num_iids = None
		self.outer_code = None
		self.track_iids = None

	def getapiname(self):
		return 'taobao.taobaoke.widget.items.convert'
