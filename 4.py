#!/usr/bin/env python3

print('一个简单的累加统计程序')
record=[]
while True:
    num=input('请输入数字:')
    if num:
        try:
            num=int(num)
            record.append(num)
        except ValueError:
            print('输入错误，请输入数字')
    else:
        break

if len(record):
    print('输入数字为:{}'.format(record))
    print('输入数字个数:{}'.format(len(record)))
    print('输入总和:{}'.format(sum(record)))
    print('最大值为:{}'.format(max(record)))
    print('最小值为:{}'.format(min(record)))
    print('平均值为:{}'.format(sum(record)/len(record)))
    
