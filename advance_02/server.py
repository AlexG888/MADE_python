from sys import argv
from threading import Thread, Lock
import socket
from queue import Queue

import requests
from bs4 import BeautifulSoup
import json


def connection(addr1, addr2):
    sock1 = socket.socket()
    sock2 = socket.socket()
    sock1.bind(("", addr1))
    sock2.bind(("", addr2))
    sock1.listen(5)
    sock2.listen(5)
    client1 = sock1.accept()[0]
    client2 = sock2.accept()[0]
    return client1, client2, sock1, sock2


def get_words_freq_dict(queue, num, lock, client, k):
    while True:
        url = queue.get()
        if url == "-":
            queue.put(url)
            break
        try:
            req = requests.get(url, timeout=2)
        except requests.exceptions.ReadTimeout:
            result = json.dumps({url: "error"}, ensure_ascii=False)
        except requests.ConnectionError:
            result = json.dumps({url: "error"}, ensure_ascii=False)
        except requests.exceptions.MissingSchema:
            result = json.dumps({url: "error"}, ensure_ascii=False)
        else:
            html_text = req.text
            soup = BeautifulSoup(html_text, "lxml")
            text = soup.get_text()
            text = text.replace("\n", " ")
            text = (
                text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
            )
            text = text.lower()
            words = text.split()
            words.sort()
            words_dict = dict()
            for word in words:
                if word in words_dict:
                    words_dict[word] = words_dict[word] + 1
                else:
                    words_dict[word] = 1
            sorted_dict = dict(
                sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[: int(k)]
            )
            result = {url: sorted_dict}
        client.send(json.dumps(result).encode("utf-8"))
        with lock:
            num[0] += 1
            print(num[0], "urls processed")


def get_url(queue, client):
    while True:
        urls = client.recv(4096).decode("utf-8").split("\n")
        for url in urls:
            if url:
                queue.put(url)
            if url == "-":
                return None


def server(workers_number, k, addr=7500):
    client1, client2, sock1, sock2 = connection(addr, addr + 100)
    lock = Lock()
    queue = Queue()
    num = [0]

    threads = [
        Thread(target=get_words_freq_dict, args=(queue, num, lock, client2, k))
        for _ in range(workers_number + 1)
    ]
    threads.append(Thread(target=get_url, args=(queue, client1)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    sock1.close()
    sock2.close()


if __name__ == "__main__":
    W = int(argv[2])
    K = int(argv[4])
    server(W, K)
