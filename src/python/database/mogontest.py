# encoding=utf-8
'''
Created on 2012-9-22

@author: wangliang
'''
import pymongo
import datetime
from pymongo import ASCENDING, DESCENDING

def print_reord(data,sort='author',order=1):
    for item in posts.find(data).sort(sort,order):   #返回的是字典
        print "item's author  is ",item['author']
    pass

connection=pymongo.Connection('localhost',27017)
db = connection.mydatabase                  # db = connection['mydatabase']
collection = db.myconn                      #collection = db['myconn']

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

posts = db.posts
#id = posts.insert(post) 
#id = posts.save(post) 
#print 'id is ',id
print 'Collection name is ',db.collection_names()
count = posts.find({"author": "Mike"}).count()
if count > 0:
    print 'In collection record(author is Mike) number is ',count
    for item in posts.find({"author": "Mike"}):
        print 'item is (author is Mike)',item
    pass
else:
    print 'In collection has no record ,insert one'
    id = posts.save(post) 
    

print 'The first record ',posts.find_one()


new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
             
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
posts.remove({})
posts.insert(new_posts)     #插入多个记录,save不行
print_reord({},order = -1)
d = datetime.datetime(2009, 11, 12, 12)

print_reord({"date": {"$lt": datetime.datetime(2009, 11, 12, 12)}})     #db.posts.find({ 'date':{'$lt':new Date('03/28/2010')}}).sort({author:-1})

print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
print posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]
posts.create_index([("date", DESCENDING), ("author", ASCENDING)])       #db.posts.find({date:{'lt':new Date('10/10/1012')}}).explain();


print posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
print posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]

#插入{ "_id" : ObjectId("505d6843e083920a070bf23f"), "date" : ISODate("2012-09-22T07:26:59.466Z"), "text" : "My first blog post!", "tags" : [ "mongodb", "python", "pymongo" ], "author" : "Mike" }


#http://serholiu.com/python-mongodb