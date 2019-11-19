
# Squared Integers using list comprehension

a_list = [1, '4', 9, 'a', 0, 4]

#对旧list操作 并复制到新的list中
#对是int型的数据进行2次放运算，存到新的list
squared_ints = [ e**2 for e in a_list if type(e) == int ]

print (squared_ints)
# [ 1, 81, 0, 16 ]


# Dict Comprehension 字典
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = { k:v**2 for (k,v) in dict1.items() }
print(double_dict1)

double_key_dict = { k*2:v**2 for (k,v) in dict1.items() }
print(double_key_dict)

#test
list2 = [i for i in range(10)]
print(list2)
list3 = [a for a in list2 if a%2==0]
print(list3)

dict2 = {'a':1,'b':'haha','c':21}
print(dict2)

dict2_1 = { k:v**2 for (k,v) in dict2.items() if type(v) == int}
print(dict2_1)