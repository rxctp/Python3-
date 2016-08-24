import collections
People=collections.namedtuple('People','ID forename middlename surname department')
data=[]
with open('test.txt',encoding='utf-8') as f:
    for line in f:
        data.append(People(*(line.split(':'))))
        
print('{0:<20}{1:<6}{2:<20}'.format('Name','ID','Username'))
print('{0:20}{1:6}{2:20}'.format('-'*16,'-'*4,'-'*10))
username_set=set()
data_list=[]
for d in data:
    username=''
    if d.middlename:
        name='{0.surname},{0.forename} {0.middlename}'.format(d)
        username=d.forename[0]+d.middlename[0]+d.surname
    else:
        name='{0.surname},{0.forename}'.format(d)
        username=d.forename[0]+d.surname
    ID='({})'.format(d.ID)
    if username not in username_set:
        username_set.add(username)
    else:
        index=1
        while True:
            if (username+str(index)) in username_set:
                index+=1
            else:
                username+=str(index)
                username_set.add(username)
                break
    msg='{0:.<19}{1:<7}{2}'.format(name[:15],ID,username.lower())
    data_list.append((d.surname,d.forename,msg))

for i in sorted(data_list):
    print(i[2])
