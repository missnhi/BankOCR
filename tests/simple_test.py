import unittest
from src import parser


class TestParser(unittest.TestCase):

    def should_parse_zeros(self):
        with open('test_data/zeros.txt') as file:
            self.assertEqual(parser.parse(file.read()), '000000000')
