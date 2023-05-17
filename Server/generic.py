import socket as k
import mimetypes
import sys

s = k.socket(k.AF_INET, k.SOCK_STREAM)
s.bind(("0.0.0.0", int(sys.argv[1])))
s.listen(5)

while True:
  c, _ = s.accept()
  try:
    path = c.recv(1024).decode().split()[1]
    c.send(f"HTTP/1.1 200 OK\nContent-Type: {mimetypes.guess_type(f'.{path}')}\n\n".encode() + open(f'.{path}', 'rb').read())
  except FileNotFoundError, IsADirectoryError: c.send("HTTP/1.1 404 Not Found".encode("utf-8"))