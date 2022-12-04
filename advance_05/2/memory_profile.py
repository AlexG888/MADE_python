import random
import weakref
import names
from memory_profiler import profile


class EmployeeRegular:
    def __init__(self, name, experience, roi):
        self.name = name
        self.experience = experience
        self.roi = roi


class EmployeeSlots:
    __slots__ = ("name", "experience", "roi")

    def __init__(self, name, experience, roi):
        self.name = name
        self.experience = experience
        self.roi = roi


def gen_data():
    while True:
        yield names.get_full_name(), random.randint(0, 10), round(
            random.uniform(0, 3), 2
        )


def work_with_data(lst):
    for obj in lst:
        if isinstance(obj, weakref.ReferenceType):
            obj_name = obj().name
            obj_experience = obj().experience
            obj_roi = obj().roi
            obj().name += "qwerty"
            obj().experience += 1
            del obj
        else:
            obj_name = obj.name
            obj_experience = obj.experience
            obj_roi = obj.roi
            obj.name += "qwerty"
            obj.experience += 1
            del obj


@profile
def regular_stat():
    lst_regular = [EmployeeRegular(*next(gen_data())) for _ in range(N)]
    work_with_data(lst_regular)


@profile
def slots_stat():
    lst_slots = [EmployeeSlots(*next(gen_data())) for _ in range(N)]
    work_with_data(lst_slots)


@profile
def weakref_stat():
    tmp = [EmployeeRegular(*next(gen_data())) for _ in range(N)]
    lst_weakref = [weakref.ref(i) for i in tmp]
    work_with_data(lst_weakref)


if __name__ == "__main__":
    N = 10_000
    regular_stat()
    slots_stat()
    weakref_stat()
