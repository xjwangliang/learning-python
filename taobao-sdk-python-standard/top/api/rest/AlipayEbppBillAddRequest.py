'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class AlipayEbppBillAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.auth_token = None
		self.bill_date = None
		self.bill_key = None
		self.charge_inst = None
		self.merchant_order_no = None
		self.mobile = None
		self.order_type = None
		self.owner_name = None
		self.pay_amount = None
		self.service_amount = None
		self.sub_order_type = None
		self.traffic_location = None
		self.traffic_regulations = None

	def getapiname(self):
		return 'alipay.ebpp.bill.add'