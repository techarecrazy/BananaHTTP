import socket as k
import re
s = k.socket()

s.bind(("", 8080))

s.listen(5)

while 1:

  c=s.accept()[0]
  
  path='.'+c.recv(1024).decode().split()[1]
  if ".." in re.split("/",path): c.send(b"HTTP/1.1 200 OK\n\n Please don't access our secret files - The admin of the server"); c.close()
  if path.endswith("/"): path+="index.html"

  try: c.send(b"HTTP/1.1 200 OK\n\n"+open(path, 'rb').read())

  except: c.send(b"HTTP/1.1 404 Not Found")

  c.close()
