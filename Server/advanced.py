import socket as k

s = k.socket()
s.bind(("", 8080))
s.listen(5)

while 1:
  c=s.accept()[0]
  response=c.recv(1024).decode()
  path='.'+response.split()[1]
  method=response.split()[0]
  if method == "GET":
      if path.endswith("/"): path+="index.html"
      try: c.send(b"HTTP/1.1 200 OK\n\n"+open(path, 'rb').read())
      except: c.send(b"HTTP/1.1 404 Not Found")
  if method == "POST":
    #TODO: Implement Post method
    c.send("HTTP/1.1 501 Not Implemented")
  c.close()
