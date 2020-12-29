import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature 1:
The method should be able to run with any number of numbers
'''
add = string_adder("10,10,2,3,4","11,22")
print("Expected Result: ", 62)
print("Result from string adder: ", add)