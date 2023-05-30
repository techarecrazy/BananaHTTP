import socket as k
import mimetypes as m

s = k.socket()
s.bind(("", 8080))
s.listen(5)

def respond(a,b): a.send(b"HTTP/1.1 200 OK\n\n"+b

while 1:
  c=s.accept()[0]
  path='.'+c.recv(1024).decode().split()[1]
  mime=m.guess_type(path)
  if ".." in path: c.send("HTTP/1.1 403 Forbidden")
  if "audio/" in mime: respond(c, open("audio.html", 'rb').read().format(path=path)))
  if "video/" in mime: respond(c, open("video.html", 'rb').read().format(path=path)))
  if path.endswith("/"): path+="index.html"
  try: respond(c, path)
  except: c.send(b"HTTP/1.1 404 Not Found")
  c.close()
