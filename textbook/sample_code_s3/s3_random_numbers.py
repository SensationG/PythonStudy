import random

# random.random(): 產生 0.0 - 1.0 (不含1.0) 的亂數
r_num = random.random()
print("random.random() 產生 0.0 - 1.0 (不含1.0) 的亂數: ", r_num)
print()

# random.randint(a, b): 隨機產生 [a, b] 之間的整數
r_int = random.randint(0, 9)
print("random.randint(a, b) 隨機產生 [a, b] 之間的整數 n, a <= n <= b:", r_int )
print()

# random.choice(seq): 從名單中隨機挑出一個值
list = ['apple', 'banana', 'coconut', 'peach']
print("random.choice 從樣本名單中隨機挑出一個值: ", random.choice(list))
print("random.choice 從樣本名單中隨機挑出一個值: ", random.choice(range(100)))
print()

# random.sample(list, k=n): 從樣本中隨機挑出不重覆的n個值
samples = random.sample(range(100), k=5) #k=5 挑出5个值
print("random.sample(list, k=n) 從樣本中隨機挑出n個值: ", samples)
print()

# random.choices(list, k=n) 從樣本中隨機挑出可能重覆的n個值
list = [20, 30, 40, 50 ,60, 70, 80, 90]
samples = random.choices(list, k=5)
print("random.choices(list, k=n) 從樣本中隨機挑出n個值 ", samples)
print()