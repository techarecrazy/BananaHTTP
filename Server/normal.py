import socket as k

s = k.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  path='.'+c.recv(1024).decode().split()[1]
  if path.endswith("/"): path+="index.html"
  if ".." in path: c.send("HTTP/1.1 403 Forbidden")
  try: c.send(b"HTTP/1.1 200 OK\n\n"+open(path, 'rb').read())
  except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
