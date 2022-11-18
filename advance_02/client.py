from sys import argv
import threading
import socket
import json


def reader(url, semaphore):
    with semaphore:
        sock.send(url.encode())
        data = sock.recv(1024)
        print(json.loads(data.decode()))


def batch_reader(filename, semaphore):
    with open(filename, encoding="utf8") as file:
        for url in file.readlines():
            reader(url, semaphore)


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(("localhost", 7500))
    m, filename = int(argv[1]), argv[2]
    sem = threading.Semaphore(m)
    threads = [
        threading.Thread(
            target=batch_reader,
            args=(filename, sem),
        )
        for _ in range(m)
    ]
    for th in threads:
        th.start()
