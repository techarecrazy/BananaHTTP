import socket as k
import os

s = k.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  path='.'+c.recv(1024).decode().split()[1]
  elif ".." or "//" in path: c.send("HTTP/1.1 403 Forbidden")
  if path.endswith("/"): 
    t="<html><body><h1>Directory listing:</h1><br>"
    for f in os.listdir(): if f != "index.html": t += f"<a href="{f}">{f}</a><br>"; else: path += "index.html"
    t+="</body></html>"
    c.send(b"HTTP/1.1 200 OK\n\n"+t.encode())
  else: send(c)
  def send(c):
    try: c.send(b"HTTP/1.1 200 OK\n\n"+with open(path, 'rb') as f: f.read(); f.close())
    except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
