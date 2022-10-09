from class_solution import CustomList

assert CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]) == CustomList([4, -1, -4, 7])
assert CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]) == CustomList([6, 3, 10, 7])
assert type(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])) == type(CustomList([5, 1, 3, 7]))
assert [1, 2] + CustomList([3, 4]) == CustomList([4, 6])
assert [1, 2] - CustomList([3, 4]) == CustomList([-2, -2])
assert CustomList([3, 4]) + [1, 2] == CustomList([4, 6])
assert CustomList([3, 4]) - [1, 2] == CustomList([2, 2])
l1, l2 = CustomList([5, 1, 3, 7]), CustomList([1, 2, 7])
assert l1 == CustomList([5, 1, 3, 7]) and l2 == CustomList([1, 2, 7])
assert (CustomList([5, 7]) > CustomList([1, 2, 7])) == True
assert (CustomList([5, 7]) == CustomList([7, 5])) == True

print(CustomList([1, 2, 7]) + CustomList([5, 1, 3, 7]))
