import sys
sys.path.insert(1, '/Users/ajayguru/Desktop/tdd-kata/src')
from main import string_adder
'''
feature5: 
Numbers bigger than 1000 should be ignored by the adder
'''

add = string_adder("1","/n2,2000")
print("Expected Result: ", 3)
print("Result from string adder: ", add)