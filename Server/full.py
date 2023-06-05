import socket as k
import os

s = k.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  try: path='.'+c.recv(1024).decode().split()[1]
  except IndexError: continue;
  if os.path.isdir(path): path += "/"
  if ".." or "//" in path: c.send(b"HTTP/1.1 403 Forbidden")
  if path[-1]=="/":
    t=""
    for f in os.listdir(path): t+=f"<a href='{f}'>{f}</a><br>"
    c.send(b"HTTP/1.1 200 OK\n\n<html><body><h1>Directory listing:</h1><br>"+t.encode()+b"</body></html>")
  else:
    try: 
      with open(path, 'rb') as f:
        c.send(b"HTTP/1.1 200 OK\n\n"+f.read())
        f.close()
    except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
