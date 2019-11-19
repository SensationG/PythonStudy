# -*- coding: utf-8 -*-
# star_triangle.py

n = int(input("Please enter a number: "))

print()
# 上方 倒三角形
for i in range(n): # 0..n-1
  spaces = i
  stars = 2*(n-1-i) + 1 # 2*(n-i) - 1
 
  print(" "*spaces, end='')
  print("*"*stars)

# 下方 三角形
for i in range(n): # 0..n-1
  spaces = n - 1 - i
  stars = 2*i + 1
  
  print(" "*spaces, end='')
  print("*"*stars)

print()

# 另解  
for i in range(n-1, -1, -1): # n-1..0
    print(" "*(n-1-i), end='')
    print("*"*(2*i + 1))
    
for j in range(0, n):       # 0..n-1
    print(" "*(n-1-j), end='')
    print("*"*(2*j + 1))
