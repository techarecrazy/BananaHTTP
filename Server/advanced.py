import socket as k
import re

s = k.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  response=c.recv(1024).decode()
  path='.'+response.split()[1]
  if response.split()[0] == "GET":
      if path.endswith("/"): path+="index.html"
      try: c.send(b"HTTP/1.1 200 OK\n\n"+open(path, 'rb').read())
      except: c.send(b"HTTP/1.1 404 Not Found")
  if response.split()[0] == "POST": open(path, "w").write(re.split("\n\n", response))
  c.close()
