import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature3: 
adder should be able to indentify any delimiters between the strings 
'''

add = string_adder("\\1/n2","\\3,4/n")
print("Expected Result: ", 1+2+3+4)
print("Result from string adder: ", add)