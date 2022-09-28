def merge(lst, tp):
    return sorted(set(lst).intersection(list(tp)))


lst = [1, 1, 2, 5, 7]
tp = (1, 1, 2, 3, 4, 7)
res = merge(lst, tp)
assert res == [1, 2, 7]
print("OK")

lst = [1, 1]
tp = (2, 3, 4, 7)
res = merge(lst, tp)
assert res == []
print("OK")

lst = [1, 1, 1, 1]
tp = (1, 1, 1, 1)
res = merge(lst, tp)
assert res == [1]
print("OK")