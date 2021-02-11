import time
import datetime

x = datetime.datetime.now()
print(x)

print(time.time())

print(time.localtime(time.time()))

tup=(2021,2,11,14,35,12,3,42,0)
print(time.mktime(tup))