import numpy


def separator(nums):
    even_list = []
    odd_list = []
    for n in nums:
        if numpy.isclose(n%2, 0, rtol=1e-05, atol=1e-08, equal_nan=False):
            even_list.append(n)
        else:
            odd_list.append(n)
    return even_list, odd_list


assert separator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert separator([0, 21, 3])
assert separator([])
print("OK")

