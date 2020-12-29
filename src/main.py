import numpy as np
import pandas as pd 
import re

def string_adder(string1,string2):
    """
    docstring
    """
    check_flag_1 = 1
    check_flag_2 = 1
    result = 0
    if not string1:
        check_flag_1 = 0
    if not string2:
        check_flag_2 = 0
    if(check_flag_1 == 1 and check_flag_2 == 1):
        # elements_2 = re.findall(r'\d+', string2)
        # elements_1 = re.findall(r'\d+', string1)
        elements_2 = [int(d) for d in re.findall(r'-?\d+', string2)]
        elements_1  = [int(d) for d in re.findall(r'-?\d+', string1)]
        for element in elements_2:
            element = int(element)
            if(element < 0):
                return Exception("negatives not allowed")
            if element > 1000:
                element = 0
                pass    
            result = result + int(element)

        for element in elements_1:
            result = result + int(element)   

    elif(check_flag_1 == 0 and check_flag_2 == 1):
        # elements_2 = re.findall(r'\d+', string2)
        elements_2 = [int(d) for d in re.findall(r'-?\d+', string2)]
        for element in elements_2:
            if(element < 0):
                return Exception("negatives not allowed")
            if element > 1000:
                element = 0
                pass    
            result = result + int(element)
    elif(check_flag_1 == 1 and check_flag_2 == 0):
        # elements_1 = re.findall(r'\d+', string1)
        elements_2 = [int(d) for d in re.findall(r'-?\d+', string1)]
        for element in elements_1:
            if(element < 0):
                return Exception("negatives not allowed")
            if element > 1000:
                element = 0
                pass    
            result = result + int(element)

    return result



if __name__ == "__main__":
    pass
    # adder = string_adder("1","2")