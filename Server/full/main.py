import socket
import mimetypes as m
import re

s = socket.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  p='.'+c.recv(1024).decode().split()[1]
  mi = m.guess_type(path))[0]
  if ".." in path: c.send("HTTP/1.1 403 Forbidden")
  if re.split('/', mi in ("video", "audio"): c.send(open(mi+".html", 'rb').read().format(p=p))
  if p.endswith("/"): p+="index.html"
  try: c.send(b"HTTP/1.1 200 OK\n\n"+open(p, "rb").read())
  except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
