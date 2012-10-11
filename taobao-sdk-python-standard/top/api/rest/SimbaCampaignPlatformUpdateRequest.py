'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaCampaignPlatformUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.nick = None
		self.nonsearch_channels = None
		self.outside_discount = None
		self.search_channels = None

	def getapiname(self):
		return 'taobao.simba.campaign.platform.update'
