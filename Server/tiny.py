s = __import__("socket").socket()
s.bind(("",8080))
s.listen(1)

while 1:
  c = s.accept()[0]
  try: r= b"HTTP/1.1 200 OK\n\n" + open(str(c.recv(1024)).split()[1][1:],'rb').read()
  except: r= b"HTTP/1.1 404 Not Found"
  c.send(r)
  c.close()
