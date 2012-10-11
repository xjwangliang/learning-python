'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class DeliveryTemplateUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.assumer = None
		self.name = None
		self.template_add_fees = None
		self.template_add_standards = None
		self.template_dests = None
		self.template_id = None
		self.template_start_fees = None
		self.template_start_standards = None
		self.template_types = None

	def getapiname(self):
		return 'taobao.delivery.template.update'
