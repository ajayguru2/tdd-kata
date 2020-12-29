import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature2: 
adder should be able to indentify any symbol between the strings and not just comma
'''
add = string_adder("1/n2","3,4")
print("Expected Result: ", 1+2+3+4)
print("Result from string adder: ", add)