'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoProductSkuDeleteRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.product_id = None
		self.properties = None

	def getapiname(self):
		return 'taobao.fenxiao.product.sku.delete'
