from pyshort import tcp
s=tcp(8080)
while 1:
  c=s.accept()[0]
  c.send(b"HTTP/1.1 200 OK\n\n"+open("index.html",'rb').read())
