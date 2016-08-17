#!/usr/bin/env python3

zero=['* * *',
      '*   *',
      '*   *',
      '*   *',
      '* * *']
one= ['* *  ',
      '  *  ',
      '  *  ',
      '  *  ',
      '* * *']
tow= ['* * *',
      '    *',
      '* * *',
      '*    ',
      '* * *']
three=['* * *',
       '    *',
       '* * *',
       '    *',
       '* * *']
four=['*   *',
      '*   *',
      '* * *',
      '    *',
      '    *']
five=['* * *',
      '*    ',
      '* * *',
      '    *',
      '* * *']
six= ['* * *',
      '*    ',
      '* * *',
      '*   *',
      '* * *']
seven=['* * *',
       '    *',
       '    *',
       '    *',
       '    *']
eight=['* * *',
       '*   *',
       '* * *',
       '*   *',
       '* * *']
nine= ['* * *',
       '*   *',
       '* * *',
       '    *',
       '* * *']

nums=[zero,one,tow,three,four,five,six,seven,eight,nine]

def showNum(n):
    n_list=list(str(n))
    for i in range(5):
        for j in n_list:
            print(nums[int(j)][i],end='  ')
        print()

print('输入数字，将以字符画的形式输出')        
showNum(123456789)

while True:
    num=input('输入一个整数:')
    if num:
        try:
            num=int(num)
            showNum(num)
        except ValueError as err:
            print(err)
            continue
    else:
        break
