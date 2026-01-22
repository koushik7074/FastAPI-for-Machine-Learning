import redis

r=redis.Redis(host='localhost', port=6379, db=0)

try:
    if r.ping():
        print('connected to redis!')
except redis.ConnectionError:
    print('Redis connection failed!')


r.set('framework', 'FastAPI')

value = r.get('framework')
print(f"Stored value for framework: {value.decode()}")