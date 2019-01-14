#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

@author: raja.raman

source:
        

'''

import random

def get_random(start, end):
    return random.randint(start, end)

def get_random_1():
    return random.randint(1, 10)

def main():
    for x in range(20):
        #print(x)
        random_one = get_random(1, 100)
        print(random_one)        
    

if __name__ == '__main__':
    main()