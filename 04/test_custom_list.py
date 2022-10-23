import unittest
from solution_custom_list import CustomList


class TestClass(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(
            CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]), CustomList([4, -1, -4, 7])
        )
        self.assertEqual(
            CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]), CustomList([6, 3, 10, 7])
        )

        self.assertEqual([1, 2] + CustomList([3, 4]), CustomList([4, 6]))
        self.assertEqual(CustomList([3, 4]) + [1, 2], CustomList([4, 6]))
        self.assertEqual([1, 2] - CustomList([3, 4]), CustomList([-2, -2]))
        self.assertEqual(CustomList([3, 4]) - [1, 2], CustomList([2, 2]))

        self.assertEqual([1, 2, 3] + CustomList([3, 4]), CustomList([4, 6, 3]))
        self.assertEqual(CustomList([3]) + [1, 2], CustomList([4, 2]))
        self.assertEqual([1, 2] - CustomList([3, 4, 10]), CustomList([-2, -2, -10]))
        self.assertEqual(CustomList([3, 4]) - [1], CustomList([2, 4]))
        self.assertEqual(CustomList([3, 4]) + [], CustomList([3, 4]))
        self.assertEqual([] - CustomList([3, 4]), CustomList([-3, -4]))

        l1, l2 = CustomList([5, 1, 3, 7]), CustomList([1, 2, 7])
        l3 = l1 - l2
        for i, j in zip(l3, CustomList([4, -1, -4, 7])):
            self.assertEqual(i, j)

        l1, l2 = CustomList([5, 1, 3, 7]), CustomList([1, 2, 7])
        l3 = l1 + l2
        for i, j in zip(l3, CustomList([6, 3, 10, 7])):
            self.assertEqual(i, j)

        l1, l2 = [1, 2], CustomList([3, 4])
        l3 = l1 + l2
        for i, j in zip(l3, CustomList([4, 6])):
            self.assertEqual(i, j)

        l1, l2 = [1, 2], CustomList([3, 4])
        l3 = l1 - l2
        for i, j in zip(l3, CustomList([-2, -2])):
            self.assertEqual(i, j)

    def test_types(self):
        self.assertIsInstance(
            CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]), CustomList
        )
        self.assertIsInstance(
            CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]), CustomList
        )

    def test_comparisons(self):
        self.assertTrue(CustomList([5, 7]) > CustomList([1, 2, 7]))
        self.assertTrue(CustomList([5, 7]) == CustomList([7, 5]))
        self.assertTrue(CustomList([8, 8]) != CustomList([7, 5]))
        self.assertTrue(CustomList([]) < CustomList([7]))
        self.assertTrue(CustomList([1, 1, 1, 1, 1]) == CustomList([5]))
        self.assertTrue(CustomList([5, 7]) <= CustomList([8, 5]))
        self.assertTrue(CustomList([5, 7]) >= CustomList([12]))

    def test_invariability(self):
        l1, l2 = CustomList([5, 1, 3, 7]), CustomList([1, 2, 7])
        l3 = l1 + l2
        self.assertEqual(l1, CustomList([5, 1, 3, 7]))
        self.assertEqual(l2, CustomList([1, 2, 7]))
        self.assertEqual(l3, CustomList([6, 3, 10, 7]))
        for i, j in zip(l1, CustomList([5, 1, 3, 7])):
            self.assertEqual(i, j)
        for i, j in zip(l2, CustomList([1, 2, 7])):
            self.assertEqual(i, j)

    def test_str(self):
        self.assertEqual(str(CustomList([5, 1, 3, 7])), "[5, 1, 3, 7], 16")
        self.assertEqual(str(CustomList()), "[], 0")
