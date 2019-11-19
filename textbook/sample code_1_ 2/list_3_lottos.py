
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:42:46 2018

7組不重複大樂透電腦選號： 6個 1-49 的亂數
"""
import random

# Create lotto numbers without duplicates 
def createLotto(): 
    lotto = []
    n = 1
    while n <= 6:
        rn = random.randint(1, 49)
        if rn not in lotto:
            lotto.append(rn)
            n += 1
    lotto.sort()
    #print(lotto)
    return lotto
   
def main():
    lottoLst = []
    c = 1
    while c <= 7:
        newLotto = createLotto()
        if newLotto not in lottoLst:
            lottoLst.append(newLotto)
            c += 1
            print(newLotto)
        
main()