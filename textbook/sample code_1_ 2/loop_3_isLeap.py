# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:17:53 2018

不定數迴圈， break at -9999
"""

while True:
    y = eval(input("Enter a year number: "))
    if y != -9999:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            print('%d is a leap year.' % (y))
        else:
            print('%d is not a leap year.' % (y))
    else:
        break

"""
def isLeap(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print('%d is a leap year.' % (y))
    else:
        print('%d is not a leap year.' % (y))
        
def main():
    while True:
        ye = eval(input("Enter a year number: "))
        if ye != -9999:
            isLeap(ye)
        else:
            break
        
main()
""" 