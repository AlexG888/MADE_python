import threading
import argparse
import socket
import requests
from bs4 import BeautifulSoup
import queue
import json


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w")
    parser.add_argument("-k")
    return parser


def get_words_freq_dict(data, k):
    url = data
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    text = soup.get_text()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
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
    return json.dumps(result).encode()


def worker(k, que, semaphore):
    while True:
        try:
            data = que.get()
        except queue.Empty:
            continue
        if data is None:
            que.put(None)
            break
        with semaphore:
            addr.send(get_words_freq_dict(data.decode(), k))
            global cnt_workers
            cnt_workers += 1
            print(f"Обработано urls: {cnt_workers}")


def add_to_queue(que):
    que.put(addr.recv(1024))


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    que = queue.Queue(maxsize=int(namespace.w))
    sem = threading.Semaphore(int(namespace.w))
    file_len = 100
    cnt_workers = 0

    sock = socket.socket()
    sock.bind(("localhost", 7500))
    sock.listen(5)
    addr, client_sock = sock.accept()

    threads = [
        threading.Thread(
            target=worker,
            args=(namespace.k, que, sem),
        )
        for _ in range(int(namespace.w))
    ]

    for th in threads:
        th.start()

    for _ in range(file_len):
        add_to_queue(que)
    que.put(None)

    for th in threads:
        th.join()
