# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:13:29 2018

Python3 program to find maximum in arr[] 
"""

#nums = eval(input ('Enter three numbers: '))
#print(type(nums))
#arr = list(nums)
arr = [10, 324, 45, 90, 9808]

# Initialize maximum element
maximum = arr[0]
 
# Solution 1: Traverse array elements from second 
# and compare every element with current max
for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print ("Largest is: ", maximum)

# Solution 2: sort the array
arr.sort()
print("Largest is: ", arr[-1])

# Solution 3: Using the array max() method
print('Largest is: ', max(arr))
print('Min is', min(arr))

"""
def largest(arr):
    # Initialize maximum element
    max = arr[0]
 
    # Traverse array elements from second
    # and compare every element with current max
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
"""