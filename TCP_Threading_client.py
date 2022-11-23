from socket import *
import time

s = socket()

s.connect(('127.0.0.1',5001))

time.sleep(5)

s.send(b'Hello')
tm = s.recv(1024)
s.close()

print("The time of server is %s" % tm.decode('ascii'))