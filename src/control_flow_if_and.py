#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

How to use the and operator in an if statement of Python?

¿Cómo usar el operador and en una sentencia if de Python?
'''

#if expression1 and expression2 and expressionN:
#    statements

#create two boolean objects
a = False
b = True

#the validation is True only if all the expressions generate a value True
if a and b:
    print('a and b are True')
else:
    print('a is False or b is False or both are False')
