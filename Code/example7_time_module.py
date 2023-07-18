import time

print(time.gmtime())
print(time.asctime(time.gmtime()))
print(time.strftime('%Y-%M-%D', time.localtime()))