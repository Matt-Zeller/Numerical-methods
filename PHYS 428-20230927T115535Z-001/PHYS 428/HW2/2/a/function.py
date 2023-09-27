# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:45:40 2017

@author: Matt
"""

def f(x):
    for n in range(10):
        x = -16 + 6*x + 12/x
        print(x)
    return

f(2.1)
f(2.001)
f(1.9)