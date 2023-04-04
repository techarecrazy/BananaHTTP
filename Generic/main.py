import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8080))
sock.listen(1)

while True:
  client, address = sock.accept()
  try:
    client.send(f"HTTP/1.1 200 OK\n\n{open(f'.{client.recv(1024).decode().splitlines()[0].split()[1]}', 'r').read()}".encode('utf-8'))
  except FileNotFoundError:
    client.send("HTTP/1.1 404 Not Found".encode("utf-8"))
