words = """art 
hue
innk
ink
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

for word in all_valid_words:
    #tiles_left = tiles
    count = 0
    for letter in word:#遍历每个单词里的字母
        if letter not in tiles:
            break
        else:
            count += 1 #如果单词有在表中 count+1
        if len(word) == count:  ##如果单词长度等于count 
            found_words = found_words +(word, )
print(found_words)
