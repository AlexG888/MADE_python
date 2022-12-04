import random
import weakref
import cProfile
import pstats
import names


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


N = 10_000


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
        else:
            obj_name = obj.name
            obj_experience = obj.experience
            obj_roi = obj.roi
            obj.name += "qwerty"
            obj.experience += 1
        del obj


def profile_deco(func):
    stat_dict = {}

    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        prof.runcall(func, *args, **kwargs)
        if func.__name__ in stat_dict:
            stat_dict[func.__name__].add(pstats.Stats(prof))
        else:
            stat_dict[func.__name__] = pstats.Stats(prof)
        return stat_dict[func.__name__]

    return wrapper


@profile_deco
def regular_stat():
    lst_regular = [EmployeeRegular(*next(gen_data())) for _ in range(N)]
    work_with_data(lst_regular)


@profile_deco
def slots_stat():
    lst_slots = [EmployeeSlots(*next(gen_data())) for _ in range(N)]
    work_with_data(lst_slots)


@profile_deco
def weakref_stat():
    tmp = [EmployeeRegular(*next(gen_data())) for _ in range(N)]
    lst_weakref = [weakref.ref(i) for i in tmp]
    work_with_data(lst_weakref)


if __name__ == "__main__":
    regular_stat()
    slots_stat()
    weakref_stat()
    regular_stat()
    regular_stat().print_stats()
