import socket as k
import mimetypes
import sys

if len(sys.argv) < 3:
    dir = "."
else:
    dir = sys.argv[2]
if len(sys.argv) < 2:
    port = "8080"
else:
    port = sys.argv[1]

s = k.socket(k.AF_INET, k.SOCK_STREAM)
s.bind(("0.0.0.0", int(port)))
s.listen(5)

while True:
  c, _ = s.accept()
  try:
    path = c.recv(1024).decode().split()[1]
    if path == "/": path = "/index.html"
    c.send(f"HTTP/1.1 200 OK\nContent-Type: {mimetypes.guess_type(f'{dir}{path}')}\n\n".encode() + open(f'{dir}{path}', 'rb').read())
  except (FileNotFoundError, IsADirectoryError): c.send("HTTP/1.1 404 Not Found".encode("utf-8"))