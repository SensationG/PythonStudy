# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:04:46 2019

@author: hhw
"""

class Solution:
    def isValid(self, nums):
        '''
        暴力法，内存溢出
        asum=[]
        j=0
        print(nums)
        while j<len(nums):
            sum1=0
            for i in nums[j:]:
                sum1+=i
                asum.append(sum1)
            j+=1
        return max(asum)
        '''
        #动态规划
        asum=[]
        sum1=0  
        for i in nums:
            if sum1>0: #如果有正向收益  包含负数的情况 （负负相加为负）      
                sum1+=i
            else: #如果没用正向收益 令sum1为下一个
                sum1=i
            asum.append(sum1)
        return max(asum)
               
    
s=Solution()
i=[-5,6,5]
a=s.isValid(i)
print(a)