#!/usr/bin/env python
# UDP Connectionless Example - Chapter 2 - udptime.py

import socket, sys, struct, time

hostname = 'localhost'
port = 51423

host = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('', (host, port))

print "Looking for replies; press Ctrl-C to stop."
myreceive = s.recvfrom(2048) #tuple: ('\xd4.\n\xe8', ('127.0.0.1', 51423))
buf = myreceive[0]
if len(buf) != 4:
    print "Wrong-sized reply %d: %s" % (len(buf), buf)
    sys.exit(1)
unpackdata = struct.unpack("!I", buf)
secs = unpackdata[0]
secs -= 2208988800
print time.ctime(int(secs))

