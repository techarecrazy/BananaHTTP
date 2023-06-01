from pyshort import tcp
s=tcp(8080)
while 1:
  c=s.accept()[0]
  c.send(b"HTTP/1.1 200 OK\n\n"+open(c.recv(1024).decode().split()[1][1:],'rb').read())
