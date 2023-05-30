import socket
import mimetypes as m
import re

s = socket.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  path='.'+c.recv(1024).decode().split()[1]
  mime=re.split('/', m.guess_type(path))[0]
  def r(): c.send(open(mime+".html", 'rb').read().format(path=path))
  if ".." in path: c.send("HTTP/1.1 403 Forbidden")
  if mime in ["video", "audio"]: r()
  if path.endswith("/"): path+="index.html"
  try: c.send(b"HTTP/1.1 200 OK\n\n"+open(path, "rb").read())
  except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
