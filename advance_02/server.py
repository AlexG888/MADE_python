from sys import argv
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


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    que = queue.Queue(maxsize=namespace.w)
    sem = threading.Semaphore(int(namespace.w))
    cnt_workers = 0

    sock = socket.socket()
    sock.bind(("localhost", 7600))
    sock.listen(5)
    addr, client_sock = sock.accept()

    with sem:
        while True:
            data = addr.recv(1024)
            if not data:
                break
            addr.send(get_words_freq_dict(data.decode(), namespace.k))
            cnt_workers += 1
            print(f"Обработано urls: {cnt_workers}")