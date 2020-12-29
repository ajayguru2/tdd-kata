import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature6: 
Delimiters can be of any length with the following format
'''

add = string_adder("1","//[***]\n1***2***3")
print("Expected Result: ", 7)
print("Result from string adder: ", add)