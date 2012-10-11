'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class PictureUploadRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.image_input_title = None
		self.img = None
		self.picture_category_id = None
		self.title = None

	def getapiname(self):
		return 'taobao.picture.upload'
