# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:45:51 2019

@author: hhw
"""

class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
    
s=Solution()
a=s.isValid('{(})')
print(a)