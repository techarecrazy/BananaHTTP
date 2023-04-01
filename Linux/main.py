import socket
from os import system

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8080))
sock.listen(1)

while True:
  client, address = sock.accept()
  print(address)
  response = f"./website{client.recv(1024).decode().splitlines()[0].split()[1]}"
  if response == "./website/":
    response = "index.html"
    system(f"sh request.sh {response}")
  else:
    system(f"sh request.sh {response}")
  client.send(open("http.txt", "rb").read())
