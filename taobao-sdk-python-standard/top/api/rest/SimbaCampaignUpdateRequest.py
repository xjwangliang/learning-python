'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class SimbaCampaignUpdateRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.campaign_id = None
		self.nick = None
		self.online_status = None
		self.title = None

	def getapiname(self):
		return 'taobao.simba.campaign.update'
