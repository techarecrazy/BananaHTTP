import socket
import os

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 21))
    s.listen()
    while True:
        conn, addr = s.accept()
        command = conn.recv(1024).decode("utf-8")
        if command in {"get", "put", "list", "help"}:
            conn.sendall(commands[command](conn).encode("utf-8"))
        else:
            conn.sendall("Unknown command".encode("utf-8"))
        conn.close()

commands = {
    "get": lambda conn: send_file(conn),
    "put": lambda conn: receive_file(conn),
    "list": lambda conn: list_files(conn),
    "help": lambda conn: conn.sendall("Commands: get, put, list, help".encode("utf-8")),
}

def send_file(conn):
    file_name = conn.recv(1024).decode("utf-8")
    if file_name in files:
        conn.sendall(str(os.path.getsize(file_name)).encode("utf-8"))
        with open(file_name, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                conn.sendall(data)
    else:
        conn.sendall("File not found".encode("utf-8"))

def receive_file(conn):
    file_name = conn.recv(1024).decode("utf-8")
    with open(file_name, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

def list_files(conn):
    files = os.listdir()
    conn.sendall(str(files).encode("utf-8"))

if __name__ == "__main__":
    main()

