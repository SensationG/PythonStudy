# List Comprehension
#直接在list中用for循环生成数字

number_list = [x for x in range(10)]
print(number_list)

# Add a condition 0到9中 符合2倍数的加入list
number_list = [x for x in range(10) if x % 2 == 0]
print(number_list)

# nested conditions 
#满足既是3的倍数又是5的倍数
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)

# generator comprehension
triangles = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print(triangles)

# 组合 4*3=12种
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print (coloured_things)

x = (x **2 for x in range(20))
print(list(x))


