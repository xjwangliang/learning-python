'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaCampaignAreaUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.area = None
		self.campaign_id = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.campaign.area.update'
