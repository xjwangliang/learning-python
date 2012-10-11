'''
Created by auto_sdk on 2012-09-23 16:46:13
'''
from top.api.base import RestApi
class CaipiaoLotterySendbynickRequest(RestApi):
	def __init__(self,domain,port):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.lottery_type_id = None
		self.stake_count = None
		self.sweety_words = None

	def getapiname(self):
		return 'taobao.caipiao.lottery.sendbynick'
