'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WlbNotifyMessagePageGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.msg_code = None
		self.page_no = None
		self.page_size = None
		self.start_date = None
		self.status = None

	def getapiname(self):
		return 'taobao.wlb.notify.message.page.get'
