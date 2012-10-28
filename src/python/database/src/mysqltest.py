#encoding=utf-8
import _mysql
import MySQLdb
db= _mysql.connect("localhost","root","root","mysql")
conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='test', charset = "utf8", use_unicode = True)
cursor = conn.cursor()
cursor.execute ("SELECT * FROM tab_wang")
rows = cursor.fetchall ()
 
for row in rows:
    print "%s, %s" % (row[0], row[1].encode('utf-8'))
print "Number of rows returned: %d" % cursor.rowcount

#Don’t forget to close the cursor and connection, and if you’re inserting data commit before closing, because autocommit is disabled by default:
cursor.close ()
conn.commit ()
conn.close ()



conn = MySQLdb.connect (host = "localhost",user = "root",passwd = "root",db = "test")

cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "server version:", row[0]
cursor.close ()
conn.close ()



#http://www.crazyant.net/2012/06/08/python%E6%93%8D%E4%BD%9Cmysql%E5%AE%9E%E4%BE%8B%E4%BB%A3%E7%A0%81%E6%95%99%E7%A8%8B%EF%BC%88%E6%9F%A5%E8%AF%A2%E6%89%8B%E5%86%8C%EF%BC%89/