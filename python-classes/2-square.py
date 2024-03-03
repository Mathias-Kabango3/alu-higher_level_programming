#!/usr/bin/python3
''' Create class Square '''

class Square:
    ''' 
    instantiate the class 
    '''


    def __init__(self,size=0):
        ''' init size '''
        if not isinstance(size,int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('Size must be >= 0')

        self.__size = size

