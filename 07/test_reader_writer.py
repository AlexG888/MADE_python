import unittest
from unittest.mock import patch, mock_open
import solution_reader_writer as rw

class TestSolution(unittest.TestCase):
    def test_json(self):
        rw.dump_data({"x": "1"}, "example.json", writer=rw.JsonWriter())
        data = rw.read_data("example.json", reader=rw.JsonReader())
        self.assertEqual(data, {"x": "1"})
        
    def test_csv(self):
        rw.dump_data(["line1", "line2", "line3"], "example.csv", writer=rw.CsvWriter())
        data = rw.read_data("example.csv", reader=rw.TxtReader())
        self.assertEqual(data, 'line1\nline2\nline3\n')
        
    def test_txt(self):
        rw.dump_data(["line1", "line2", "line3"], "example.txt", writer=rw.TxtWriter())
        data = rw.read_data("example.txt", reader=rw.TxtReader())
        self.assertEqual(data, 'line1\nline2\nline3\n')
        
