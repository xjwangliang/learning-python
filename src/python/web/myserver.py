# encoding=utf-8
#!/usr/bin/env python
'''
Created on 2012-10-22

@author: wangliang
'''
import socket
host = ''
port = 51897
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(3)

