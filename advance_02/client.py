from sys import argv
import threading
import socket
import json


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(("localhost", 7600))
    m, filename = argv[1], argv[2]
    sem = threading.Semaphore(int(m))
    with sem:
        with open(filename, encoding="utf8") as file:
            for url in file.readlines():
                sock.send(url.encode())
                data = sock.recv(1024)
                print(json.loads(data.decode()))
