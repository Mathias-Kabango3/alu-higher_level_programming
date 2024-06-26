#!/usr/bin/python3
'''
Function (add_interger) that adds two numbers and return the result
'''

def add_integer(a,b=98):
    ''' Function that adds two integers
    Args:
        a : this must be either an integer or float
        b : Must be either an integer or float, and if not provided
            it takes the defualt value of 98
    Returns:
        an integer: the addition of a and b
    '''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    elif type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    result = a+b
    return result
