import unittest
from solution_generator import Generator


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = Generator("file_for_second_task.txt", ["Роза", "упала", "а"])

    def test_output(self):
        self.assertEqual(next(self.gen), "а Роза упала на лапу Азора\n")
        self.assertEqual(next(self.gen), "а упала\n")
        self.assertEqual(next(self.gen), "а\n")
        self.assertEqual(next(self.gen), "а Роза Азора\n")
        self.assertEqual(next(self.gen), "а Роза упала на лапу Азора\n")
        self.assertEqual(next(self.gen), "упала на лапу\n")
        self.assertEqual(next(self.gen), "упала\n")
        self.assertEqual(next(self.gen), "Роза")

    def test_exception(self):
        with self.assertRaises(StopIteration):
            next(self.gen)
            next(self.gen)
            next(self.gen)
            next(self.gen)
            next(self.gen)
            next(self.gen)
            next(self.gen)
            next(self.gen)
            next(self.gen)
