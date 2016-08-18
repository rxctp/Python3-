#配号起始数
num='47390251'
#配号数量
count=3
#配号提取
total_values=[]
#分割符
sign='、'
#中签末4位
end_four='4252、9252'.split(sign)
#中签末5位
end_five='92567、05067、17567、30067、42567、55067、67567、80067'.split(sign)
#中签末6位
end_six='607027、807027、007027、207027、407027、560421、810421、060421、310421'.split(sign)
#中签末7位
end_seven='1390251、3390251、5390251、7390251、9390251、2093379、7093379'.split(sign)
#中签末8位
end_eight='02476990、14976990、27476990、39976990、52476990、64976990、77476990、89976990'.split(sign)
#中签末9位
end_nine='057952262'
#中签号整合
total_choice=[end_four,end_five,end_six,end_seven,end_eight,end_nine]

nums=[str(int(num)+n) for n in range(count)]
print('获得配号:',nums)
print("="*50)

def print_msg(n):
    values=[]
    for i in nums:
        if n>len(i):
            continue
        values.append(i[-n:])
    if values:
        #print("末{}位:".format(n))
        #print(values)
        total_values.append(values)
        
    

for i in range(4,10):
    print_msg(i)

getNum=False

for i in range(6):
    try:
        for num in total_choice[i]:
            if num in total_values[i]:
                getNum=True
                print('末{}位 中签号码：{}'.format(i+4,num))
    except IndexError:
        pass

if getNum:
    print('程序结束,恭喜中签')
else:
    print('很遗憾本次未中签，下次继续')
