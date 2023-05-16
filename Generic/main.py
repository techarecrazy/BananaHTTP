import socket as k

s = k.socket(k.AF_INET, k.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen(5)

while True:
  c, _ = s.accept()
  try:
    c.send(f"HTTP/1.1 200 OK\n\n{open('.{c.recv(1024).decode().splitlines()[0].split()[1]}', 'r').read()}".encode())
  except (FileNotFoundError, IsADirectoryError): 
    c.send("HTTP/1.1 404 Not Found".encode("utf-8"))
