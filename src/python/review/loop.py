i = 0
while i<10:
	print i
	i += 1

for line in open("readme.txt"):
	print line
	
	
data =('string',100,3.1415)
for i,value in enumerate(data):
	print i,value