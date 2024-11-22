import unittest
from src.parser import parser
from src.isValidAccount import isValidAccount

class TestParser(unittest.TestCase):
    def test_parse_numbers(self):
        with open('test_data/zeros.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['000000000'])
        with open('test_data/ones.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['111111111'])
        with open('test_data/twos.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['222222222'])
        with open('test_data/threes.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['333333333'])
        with open('test_data/fours.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['444444444'])
        with open('test_data/fives.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['555555555'])
        with open('test_data/sixes.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['666666666'])
        with open('test_data/sevens.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['777777777'])
        with open('test_data/eights.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['888888888'])
        with open('test_data/nines.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['999999999'])

    def test_multiple_accounts(self):
        with open('test_data/multiple_accounts.txt') as file:
            result = parser(file.readlines())
            self.assertEqual(result, ['123456789', '999999999'])

    def test_valid_checksum(self):
        '''
        '000000051' : is a valid account number (1+5*2) mod 11 = 0
        '888888888' : is a NOT a valid account number
        '49006771? ILL' : is illegible
        '''
        with open('test_data/valid_checksum.txt') as file:
            result = isValidAccount(file.readlines())
            self.assertEqual(result, ['000000051','888888888 ERR', '49006771? ILL', '1234?678? ILL'])
