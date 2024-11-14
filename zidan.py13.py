# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:06:23 2024

@author: ASUS
"""

print("Program untuk angka ordinal")

x = False

n = ""

def make_ordinal(n):

    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    print("(", n, ",", '"',suffix,'"', ")")
while (not x):
    print("Gunakan '0' untuk menghentikan")
    n = int(input("masukan angka: ")) 
    if n == 0:
        x = True
    else:
        make_ordinal(n)
        
        