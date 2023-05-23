import socket as k

s = k.socket(k.AF_INET, k.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen(5)


while True:
  c, _ = s.accept()
  path = '.'+c.recv(1024).decode().split()[1]
  try: c.send(b"HTTP/1.1 200 OK\n\n" + open(path, 'rb').read())
  except FileNotFoundError: c.send(b"HTTP/1.1 404 Not Found")
  except IsADirectoryError: c.send(b"HTTP/1.1 200 OK\n\n" + open(path+'/index.html', 'r').read())
  except: c.send(b"HTTP/1.1 500 Internal Server Error")
