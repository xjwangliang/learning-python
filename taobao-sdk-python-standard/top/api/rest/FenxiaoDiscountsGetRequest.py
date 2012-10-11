'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoDiscountsGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.discount_id = None
		self.ext_fields = None

	def getapiname(self):
		return 'taobao.fenxiao.discounts.get'
