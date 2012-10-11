'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoProductSkuAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.agent_cost_price = None
		self.dealer_cost_price = None
		self.product_id = None
		self.properties = None
		self.quantity = None
		self.sku_number = None
		self.standard_price = None

	def getapiname(self):
		return 'taobao.fenxiao.product.sku.add'
