import socket as k

s = k.socket(k.AF_INET, k.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen(5)

while True:
  c, _ = s.accept()
  try: c.send(f"HTTP/1.1 200 OK\n\n".encode() + open(f'.{c.recv(1024).decode().split()[1]}', 'r').read())
  except FileNotFoundError: c.send("HTTP/1.1 404 Not Found".encode())