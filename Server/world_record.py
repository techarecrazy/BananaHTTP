import socket as k

s=k.socket()
s.bind(("",8080))
s.listen(5)

while 1:
  s.accept()[0].send(b"HTTP/1.1 200 OK\n\n"+open("index.html").read())
