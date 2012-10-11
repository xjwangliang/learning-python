'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class WangwangEserviceChatlogGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.from_id = None
		self.start_date = None
		self.to_id = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.chatlog.get'
