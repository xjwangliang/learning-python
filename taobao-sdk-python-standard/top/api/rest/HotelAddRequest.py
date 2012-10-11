'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class HotelAddRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.address = None
		self.city = None
		self.country = None
		self.decorate_time = None
		self.desc = None
		self.district = None
		self.domestic = None
		self.level = None
		self.name = None
		self.opening_time = None
		self.orientation = None
		self.pic = None
		self.province = None
		self.rooms = None
		self.service = None
		self.site_param = None
		self.storeys = None
		self.tel = None

	def getapiname(self):
		return 'taobao.hotel.add'
