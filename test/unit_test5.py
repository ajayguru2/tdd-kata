import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature4: 
adder should be able to indentify any non negative numbers and throw exception.
'''

add = string_adder("1","/n-2")
print("Expected Result: ", "Exception")
print("Result from string adder: ", add)