# encoding=utf-8
'''
Created on 2012-9-24

@author: wangliang
'''

#注册微博App后，可以获得app key和app secret，然后定义网站回调地址：

from weibo import APIClient
from idlelib.IOBinding import encoding

APP_KEY = '1234567' # app key
APP_SECRET = 'abcdefghijklmn' # app secret
CALLBACK_URL = 'http://www.example.com/callback' # callback url


#在网站放置“使用微博账号登录”的链接，当用户点击链接后，引导用户跳转至如下地址：

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
# TODO: redirect to url



