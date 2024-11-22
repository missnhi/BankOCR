'''
dataBuilder.py is a helper function that reads the test data from the test_data folder
and builds a dictionary with the key as the number and the value as the digit that
the number represents.
EXAMPLE:
data = {' _ | ||_|': '0',
        '     |  |': '1',
        ' _  _||_ ': '2',
        ' _  _| _|': '3',
        '   |_|  |': '4',
        ' _ |_  _|': '5',
        ' _ |_ |_|': '6',
        ' _   |  |': '7',
        ' _ |_||_|': '8',
        ' _ |_| _|': '9'
    }
'''
from src.helperFunction.parseNumbers import parseNumbers
import os

def dataBuilder() :
    data = {}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../../tests/test_data')

    with open(os.path.join(file_path, 'zeros.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '0'
    with open(os.path.join(file_path, 'ones.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '1'
    with open(os.path.join(file_path, 'twos.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '2'
    with open(os.path.join(file_path, 'threes.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '3'
    with open(os.path.join(file_path, 'fours.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '4'
    with open(os.path.join(file_path, 'fives.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '5'
    with open(os.path.join(file_path, 'sixes.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '6'
    with open(os.path.join(file_path, 'sevens.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '7'
    with open(os.path.join(file_path, 'eights.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '8'
    with open(os.path.join(file_path, 'nines.txt')) as file:
        key = parseNumbers(file.readlines())
        data[key] = '9'
        
    return data
