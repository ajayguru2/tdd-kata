import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature7: 
Allow multiple delimiters like this: “//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.
'''

add = string_adder("//[delim][delim]\n","//[*][%]\n1*2%3")
print("Expected Result: ", 6)
print("Result from string adder: ", add)