import socket as k

s = k.socket()
s.bind(("0.0.0.0", 8080))
s.listen(5)

while 1:
  c, _ = s.accept()                                                          path = '.'+c.recv(1024).decode().split()[1]
  if path.endswith("/"): path = path + "index.html"
  try: c.send(b"HTTP/1.1 200 OK\n\n"+open(path, 'rb').read())
  except: c.send(b"HTTP/1.1 404 Not Found")
