#!/usr/bin/env python3
import random

ROWS=0
COLUMNS=1
MIN=2
MAX=3

titles=['行数','列数','最小值','最大值']
values=[]
def inputValue(title):
    while True:
        value=input("请输入需要的"+title+":")
        try:
            value=int(value)
            values.append(value)
            break
        except ValueError:
            print('输入错误，请输入整数')

for i in titles:
    inputValue(i)

for i in range(values[ROWS]):
    for j in range(values[COLUMNS]):
        value=random.randint(values[MIN],values[MAX])
        print("{:>5}".format(value),end=' ')
    print() 
