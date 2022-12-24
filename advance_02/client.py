from sys import argv
from threading import Thread
import socket
from queue import Queue


def connection(addr1, addr2):
    sock1 = socket.socket()
    sock2 = socket.socket()
    sock1.connect(("", addr1))
    sock2.connect(("", addr2))
    return sock1, sock2


def reader_url(queue, sock1, sock2):
    while not queue.empty():
        url = queue.get()
        sock1.sendall(url.encode("utf-8"))
        data = sock2.recv(4096).decode("utf-8")
        print(data)


def urls_list_maker(filename):
    with open(filename, "r", encoding="utf8") as file:
        urls_list = file.readlines()
    return urls_list


def client(thread_num, urls, addr=7500):
    sock1, sock2 = connection(addr, addr + 100)
    queue = Queue()
    for url in urls:
        if url[-1] != "\n":
            queue.put(url + "\n")
        else:
            queue.put(url)
    queue.put("-")
    threads = [
        Thread(target=reader_url, args=(queue, sock1, sock2)) for _ in range(thread_num)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    sock1.close()
    sock2.close()


if __name__ == "__main__":
    thread_number = int(argv[1])
    name = argv[2]
    urls_list = urls_list_maker(name)
    client(thread_number, urls_list)
