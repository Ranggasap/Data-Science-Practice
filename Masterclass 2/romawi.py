# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:08:41 2021

@author: rangga
"""

def int_to_rom(num):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romans = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    roman_number = ''
    i = 12
    while num != 0:
        if numbers[i] <= num:
            roman_number += romans[i]
            num = num-numbers[i]
        else:
            i -= 1
    return roman_number

print(int_to_rom(12))
print(int_to_rom(1222))
print(int_to_rom(780))
print(int_to_rom(45))

            