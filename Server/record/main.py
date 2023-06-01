from pyshort import tcp
s=tcp(8080)
while 1:
  s.send(b"HTTP/1.1 200 OK\n\nHello")
