'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class JianghuFanFollowRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.shop_owner_id = None

	def getapiname(self):
		return 'taobao.jianghu.fan.follow'
