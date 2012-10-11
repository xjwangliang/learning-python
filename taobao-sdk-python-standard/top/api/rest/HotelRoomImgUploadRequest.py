'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class HotelRoomImgUploadRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.gid = None
		self.pic = None
		self.position = None

	def getapiname(self):
		return 'taobao.hotel.room.img.upload'
