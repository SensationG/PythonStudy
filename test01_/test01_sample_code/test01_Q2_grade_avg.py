# -*- coding: utf-8 -*-

import random

# Using the following grade_dict for testing
"""
grade_dict = {'s1071202':[75, 75, 75, 75, 60, 60], 's1071235': [70, 70, 70, 70, 80, 80], 
              's1071237':[71, 72, 78, 79, 89, 98], 's1071239': [74, 85, 76, 75, 83, 86],
              's1071246':[85, 85, 85, 95, 95, 85], 's1071248': [85, 85, 95, 75, 63, 77],
              's1071250':[80, 80, 80, 80, 81, 98], 's1071253': [71, 75, 74, 75, 74, 78],
              's1071258':[72, 78, 78, 72, 97, 90], 's1071266': [74, 74, 74, 74, 65, 65]}
"""

credit_list = [3, 3, 3, 2, 2, 3]
credits = sum(credit_list)

ids = random.sample(range(1071201,1071300), k=20)
ids.sort()
grade_dict = {}

for id in ids:
  sid = 's' + str(id)
  grade_dict[sid] = random.choices(range(60, 100), k=6)
  
#print(grade_dict)

avg_dict = {} # each item: (studentId, average)

print("Student Scores and Average:")

for key, values in grade_dict.items():
    #print(key, values) # optional, just to make sure I get correct data
    stu_sum = 0
    
    for i, v in enumerate(values):
      stu_sum += v * credit_list[i]
    
    average = stu_sum/credits
    avg_dict[key] = average # store student's average to avg_dict
    print("#%s: %s, %.2f " % (key, values, average))

# sort avg_dict by student's average in descending order
v_sorted_list = sorted(avg_dict.items(), key=lambda x: x[1], reverse=True)

# print all students average
#print("Student Grade Average:")
#for k, v in avg_dict.items():
#  print("#%s: %.2f" % (k, v))

# print top 3 students and their average
print("\nTop 3 performed students")
for k, v in v_sorted_list[:3]:
    print("#%s: %.2f" % (k, v))
    

# Finding the top three
from collections import Counter 

# Create a counter object
k = Counter(avg_dict) 
  
# Finding 3 highest values 
tops = k.most_common(3)  
  
print("Dictionary with 3 highest values:")
  
for i in tops: 
    print("#%s: %.2f" % (i[0], i[1]))
