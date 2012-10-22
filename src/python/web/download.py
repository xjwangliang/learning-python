#!/usr/bin/env python
'''
Created on 2012-10-22

@author: wangliang
'''

import socket
import sys
import time
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
    print "Strange Error while creating socket %s " % e
    sys.exit(1)
    
    
port = socket.getservbyname("http","tcp")
print "port is " ,port
try:
    s.connect(("www.baidu.com",port))
except socket.gaierror,e:
    print "Address error is %s " % e
    sys.exit(1)
except socket.error,e:
    print "Connect error %s " % e
    sys.exit(1)
     
     

peername = s.getpeername()
socketname = s.getsockname()

print "peername is %s ,socketname is %s" %peername,socketname
