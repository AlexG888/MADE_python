import time


def mean(k):
    def _mean(function):
        l = []

        def wrapped(*args, **kwargs):
            start_ts = time.time()
            res = function(*args, **kwargs)
            end_ts = time.time()
            l.append(end_ts - start_ts)
            print(f"Cреднее время последних {k} вызовов: {sum(l[-k:]) / len(l[-k:])}")
            return res

        return wrapped

    return _mean


@mean(5)
def foo1(t):
    time.sleep(t)
    return 10 - 5


@mean(2)
def foo2(t):
    time.sleep(t)
    return 5 - 3


for i in range(5):
    assert foo1(1) == 5


for i in range(10):
    assert foo2(i / 10) == 2

print("OK")
