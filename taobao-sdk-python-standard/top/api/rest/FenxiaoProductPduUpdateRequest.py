'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class FenxiaoProductPduUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.distributor_id = None
		self.is_delete = None
		self.product_id = None
		self.quantity_type = None
		self.quantitys = None
		self.sku_properties = None

	def getapiname(self):
		return 'taobao.fenxiao.product.pdu.update'
