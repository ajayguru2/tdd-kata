import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
first unit test:
Function should be able to add 2 numbers given
in string format
'''
add = string_adder("","1,2")
print(add)
