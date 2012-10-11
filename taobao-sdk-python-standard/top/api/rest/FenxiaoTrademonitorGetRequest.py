'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoTrademonitorGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.distributor_nick = None
		self.end_created = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.product_id = None
		self.start_created = None

	def getapiname(self):
		return 'taobao.fenxiao.trademonitor.get'
