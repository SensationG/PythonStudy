# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:01:22 2019

@author: hhw
"""

words = """art 
hue
ink
innk
crosshatching
"""
tiles = "hijklmnopcrsatg"
all_valid_words =()
start = 0
end = 0
found_words =() 

for char in words:
    if char == "\n":
        all_valid_words = all_valid_words +(words[start:end], )
        start = end + 1
        end = end +1
    else:
        end = end + 1
print(all_valid_words)
for word in all_valid_words:
    tiles_left = tiles
    for letter in word:
        if letter not in tiles_left:
            break
        else:
            index = tiles_left.find(letter)
            tiles_left = tiles_left[:index]+tiles_left[index+1:]
 
        if len(word)== len(tiles)-len(tiles_left):
            found_words = found_words +(word, )

print(found_words)





