from itertools import zip_longest


class CustomList(list):
    def __add__(self, other):
        new_list = []
        for item in zip_longest(self, other, fillvalue=0):
            new_list.append(item[0] + item[1])
        return CustomList(new_list)

    def __radd__(self, other):
        new_list = []
        for item in zip_longest(self, other, fillvalue=0):
            new_list.append(item[0] + item[1])
        return CustomList(new_list)

    def __sub__(self, other):
        new_list = []
        for item in zip_longest(self, other, fillvalue=0):
            new_list.append(item[0] - item[1])
        return CustomList(new_list)

    def __rsub__(self, other):
        new_list = []
        for item in zip_longest(self, other, fillvalue=0):
            new_list.append(item[1] - item[0])
        return CustomList(new_list)

    def __eq__(self, other):
        return sum(self[:]) == other

    def __ne__(self, other):
        return sum(self[:]) != other

    def __lt__(self, other):
        return sum(self[:]) < other

    def __le__(self, other):
        return sum(self[:]) <= other

    def __ge__(self, other):
        return sum(self[:]) >= other

    def __gt__(self, other):
        return sum(self[:]) > other

    def __str__(self):
        return f"{self[:]}, {sum(self[:])}"
