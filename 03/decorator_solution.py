import time


def mean(k):
    def _mean(function):
        l = []

        def wrapped(*args, **kwargs):
            start_ts = time.time()
            function(*args, **kwargs)
            end_ts = time.time()
            l.append(end_ts - start_ts)
            return sum(l[-k:]) / len(l[-k:])

        return wrapped

    return _mean


@mean(5)
def foo1(t):
    time.sleep(t)
    pass


@mean(2)
def foo2(t):
    time.sleep(t)
    pass


for i in range(5):
    assert round(foo1(1), 2) == 1.0
    print(foo1(1))

test = [0.0, 0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85]
for i in range(10):
    assert round(foo2(i / 10), 2) == test[i]
    print(round(foo2(i / 10), 2))

print("OK")
