# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:19:44 2018

Calculate student grade avarage
"""

grades = [[79, 69, 89], [80, 80, 80], [64, 86, 60]]

def calcAvg(alist):
    #total = 0
    #for i in range(len(alist)):
    #    total += alist[i]
    total = sum(alist)
    average = total/len(alist)
    return average
    
def main():
    for i in range(len(grades)):
        avg = calcAvg(grades[i])
        print('#%d student, average = %.2f' % (i+1, avg))
    # enumeate(list): create a list of tuples, each is a pair (counter/index, value)
    print(list(enumerate(grades)))
    for i, grade in enumerate(grades):
        avg = calcAvg(grade)
        print('#%d student2, average = %.2f' % (i+1, avg))
main()