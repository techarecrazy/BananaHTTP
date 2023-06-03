import socket as k
import os

s = k.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  try: path='.'+c.recv(1024).decode().split()[1]
  except IndexError: continue;
  if ".." or "//" in path: c.send(b"HTTP/1.1 403 Forbidden")
  if path[-1]=="/":
    t=f"<html><body><h1>Directory listing:</h1><br>"
    for f in os.listdir(path):
      if f!="index.html": t+=f"<a href='{f}'>{f}</a><br>"
      else: path+="index.html"
    t+="</body></html>"
    c.send(b"HTTP/1.1 200 OK\n\n"+t.encode())
  else:
    try:
      with open(path, 'rb') as f:                                                                         o=f.read()
        c.send(b"HTTP/1.1 200 OK\n\n"+o)                                                                  f.close()
    except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
