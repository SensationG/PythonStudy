# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:56:18 2018

@author: User
"""

s = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation."""

line_count = word_count = char_count = 0


lines = s.splitlines()#以换行分界
#lines = s.split()  #  \r\n

line_count = len(lines)

for l in lines:
    words = l.split()
    print(words)
    
    word_count += len(words)
    for w in words:
        w = w.rstrip(',.?!') # remove 移除標點符號 
        char_count += len(w)

print("%10s = %3d" % ("Lines", line_count))
print("%10s = %3d" % ("Words", word_count))
print("%10s = %3d" % ("Characters", char_count))