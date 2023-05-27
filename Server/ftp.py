import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 21))
s.listen()
while True:
    conn, addr = s.accept()
    try: commands[conn.recv(1024).decode("utf-8")](conn)
    except: conn.sendall("Unknown command".encode("utf-8"))
    conn.close()

commands = {"get": lambda conn: try: path = conn.recv(1024).decode("utf-8"); conn.sendall(str(os.path.getsize()).encode("utf-8")); conn.sendall(open(file_name, "rb").read()); except: conn.sendall("File not found".encode("utf-8")),"put": lambda conn: while 1: data = conn.recv(1024); if not data: break; open(conn.recv(1024).decode("utf-8"), "wb").write(data),"list": lambda conn: conn.sendall(str(os.listdir()).encode("utf-8")),"help": lambda conn: conn.sendall("Commands: get, put, list, help".encode("utf-8")),