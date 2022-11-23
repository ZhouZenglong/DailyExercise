import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(b"hello",("127.0.0.1",5000))
resp,addr = s.recvfrom(512)

print(resp.decode())

s.sendto(b"world",("127.0.0.1",5000))
resp,addr = s.recvfrom(512)

print(resp.decode())

s.close()

