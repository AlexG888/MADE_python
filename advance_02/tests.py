import unittest

import os
import sys
import io
import time
from multiprocessing import Queue, Process
from server import server
from client import client


def server_wrapper(thread_num, k, addr):
    with open(os.devnull, "w", encoding="utf8") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        server(thread_num, k, addr)
        sys.stdout = old_stdout


def client_wrapper(requests_num, urls, que, addr):
    new_stdout = io.StringIO(initial_value="", newline="\n")
    old_stdout = sys.stdout
    sys.stdout = new_stdout
    client(requests_num, urls, addr)
    que.put(new_stdout.getvalue())
    sys.stdout = old_stdout
    new_stdout.close()


class TestClientServer(unittest.TestCase):
    def setUp(self):
        self.addr = 7500

    def test_right_urls(self):
        urls = [
            "https://www.magazines.com/",
            "https://www.allrecipes.com",
        ]

        queue = Queue()
        proc_1 = Process(target=server_wrapper, args=(2, 7, self.addr))
        proc_2 = Process(target=client_wrapper, args=(2, urls, queue, self.addr))

        proc_1.start()
        time.sleep(1)
        proc_2.start()

        proc_1.join()
        proc_2.join()

        answ1 = (
            '{"https://www.magazines.com/": {"magazines": 3, "cookies": 2, "magazine": 2, '
            '"newsstand": 2, "|": 2, "2022": 1, "a-z": 1}}'
        )
        answ2 = (
            '{"https://www.allrecipes.com": {"save": 23, "ratings": 20, "&": 17, "all": '
            '15, "view": 15, "the": 11, "christmas": 10}}'
        )

        results = sorted([s for s in queue.get().split("\n") if s])
        answers = sorted([answ1, answ2])
        self.assertEqual(results, answers)

    def test_bad_url(self):
        urls = ["bad_url"]
        queue = Queue()
        proc_1 = Process(target=server_wrapper, args=(2, 7, self.addr + 200))
        proc_2 = Process(target=client_wrapper, args=(2, urls, queue, self.addr + 200))

        proc_1.start()
        time.sleep(1)
        proc_2.start()

        proc_1.join()
        proc_2.join()

        result = queue.get()
        while result[-1] == "\n":
            result = result[1:-3]
        answer = r"{\"bad_url\": \"error\"}"
        self.assertEqual(result, answer)


if __name__ == "__main__":
    unittest.main()
