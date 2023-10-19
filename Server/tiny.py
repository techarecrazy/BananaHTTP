import socket.socket

s = socket()
s.bind(("",8080))
s.listen(1)

while 1:
  c = s.accept()[0]
  try: c.send(b"HTTP/1.1 200 OK\n\n" + open(str(c.recv(1024)).split()[1][1:],'rb').read())
  except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
