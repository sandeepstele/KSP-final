'''a=[]
with open('2/profession.txt','r') as f:
    for line in f:
        a.append(line.strip())
print(a)'''

import random

base_color = ["#7267EF", "#0e9e4a", "#3ec9d6", "#ffa21d", "#EA4D4D"]
random_color=[]

for _ in range(30):
    random_colors = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    random_color.append(random_colors)
print(random_color)
