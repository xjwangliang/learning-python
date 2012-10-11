'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class HotelTypeAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.hid = None
		self.name = None
		self.site_param = None

	def getapiname(self):
		return 'taobao.hotel.type.add'
