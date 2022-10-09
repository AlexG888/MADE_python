from itertools import zip_longest


class CustomList(list):
    def __new__(cls, value):
        obj = super().__new__(cls, value)
        return obj

    def __init__(self, incoming_list):
        super().__init__(incoming_list)
        self.mylist = incoming_list
        self.sum_list = sum(self.mylist)

    def __add__(self, other):
        new_list = []
        if hasattr(other, "mylist"):
            for item in zip_longest(self.mylist, other.mylist, fillvalue=0):
                new_list.append(item[0] + item[1])
        else:
            for item in zip_longest(self.mylist, other, fillvalue=0):
                new_list.append(item[0] + item[1])
        return CustomList(new_list)

    def __radd__(self, other):
        new_list = []
        if hasattr(other, "mylist"):
            for item in zip_longest(self.mylist, other.mylist, fillvalue=0):
                new_list.append(item[0] + item[1])
        else:
            for item in zip_longest(self.mylist, other, fillvalue=0):
                new_list.append(item[0] + item[1])
        return CustomList(new_list)

    def __sub__(self, other):
        new_list = []
        if hasattr(other, "mylist"):
            for item in zip_longest(self.mylist, other.mylist, fillvalue=0):
                new_list.append(item[0] - item[1])
        else:
            for item in zip_longest(self.mylist, other, fillvalue=0):
                new_list.append(item[0] - item[1])
        return CustomList(new_list)

    def __rsub__(self, other):
        new_list = []
        if hasattr(other, "mylist"):
            for item in zip_longest(self.mylist, other.mylist, fillvalue=0):
                new_list.append(item[1] - item[0])
        else:
            for item in zip_longest(self.mylist, other, fillvalue=0):
                new_list.append(item[1] - item[0])
        return CustomList(new_list)

    def __eq__(self, other):
        return self.sum_list == other

    def __ne__(self, other):
        return self.sum_list != other

    def __lt__(self, other):
        return self.sum_list < other

    def __le__(self, other):
        return self.sum_list <= other

    def __ge__(self, other):
        return self.sum_list >= other

    def __gt__(self, other):
        return self.sum_list > other

    def sum_dec(func):
        def wrapper(self, *args, **kw):
            print("Cумма элементов массива: {}".format(self.sum_list))
            return func(self, *args, **kw)

        return wrapper

    @sum_dec
    def __str__(self):
        return str(self.mylist)
