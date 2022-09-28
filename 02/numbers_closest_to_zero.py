from numpy import inf, isclose


def numbers_closest_to_zero(arr):
    closest_to_zero = inf
    result = []
    for i in arr:
        if abs(i) < closest_to_zero:
            closest_to_zero = abs(i)
            result = [i]
        elif isclose(abs(i), closest_to_zero, rtol=1e-05, atol=1e-08, equal_nan=False):
            result.append(i)
    return result


print(numbers_closest_to_zero([0, 1, 2, 3, 4, 5]))
print(numbers_closest_to_zero([-100000, 1, 4, 56, 4, 1, 1]))
print(numbers_closest_to_zero([-0.32423, -1, 4.34232, 56, 0.32423]))
print("OK")
