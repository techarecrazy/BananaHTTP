import socket
def tcp(port):
  s = socket.socket()
  s.bind(("", port))
  s.listen(5)
  return s.accept()[0]
