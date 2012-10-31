#encoding=utf-8
import redis
r = redis.Redis(host='localhost', port=6379, db=0)   #如果设置了密码，就加上password=密码
print "get foo",r.delete('foo')
print "delete foo"
print "get foo",r.delete('foo')
print r.get('foo')   
print "dbsize:",r.dbsize()

r = redis.StrictRedis(host='127.0.0.1', port=6379)
r.set('foo', 'hello')
r.rpush('mylist', 'one')
print r.get('foo')
print r.rpop('mylist')

#redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
#可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池

pool = redis.ConnectionPool(host='127.0.0.1', port=9212)
r = redis.Redis(connection_pool=pool)
r.set('one', 'first')
r.set('two', 'second')
print r.get('one')
print r.get('two')


#redis pipeline机制，可以在一次请求中执行多个命令，这样避免了多次的往返时延。
 
pool = redis.ConnectionPool(host='127.0.0.1', port=9212)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline()
pipe.set('one', 'first')
pipe.set('two', 'second')
pipe.execute()
 
pipe.set('one','first').rpush('list', 'hello').rpush('list', 'world').execute()

