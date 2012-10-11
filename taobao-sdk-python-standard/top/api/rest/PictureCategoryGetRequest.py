'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class PictureCategoryGetRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.modified_time = None
		self.parent_id = None
		self.picture_category_id = None
		self.picture_category_name = None
		self.type = None

	def getapiname(self):
		return 'taobao.picture.category.get'
