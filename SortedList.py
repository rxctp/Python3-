_identity=lambda x:x

class SortedList:
    
    def __init__(self,sequence=None,key=None):
        self.__key=key or _identity
        assert hasattr(self.__key,"__call__")
        if sequence is None:
            self.__list=[]
        elif (isinstance(sequence,SortedList) and sequence.key==self.__key):
            self.__list=sequence.__list[:]
        else:
            self.__list=sorted(list(sequence),key=self.key)
    
    @property
    def key(self):
        return self.__key

    def add(self,value):
        index=self.__bisect_left(value)
        if index==len(self.__list):
            self.__list.append(value)
        else:
            self.__list.insert(index,value)

    def __bisect_left(self,value):
        key=self.__key(value)
        left,right=0,len(self.__list)
        count=0
        while left<right:
            count+=1
            print('已迭代次数{}'.format(count))
            middle=(left+right)//2
            print("左边界:{} 中值:{} 右边界{}".format(left,middle,right))
            if self.__key(self.__list[middle])<key:
                left=middle+1
            else:
                right=middle
        #print('已迭代次数{}'.format(count))
        return left

    def remove(self,value):
        index=self.__bisect_left(value)
        if index<len(self.__list) and self.__list[index]==value:
            del self.__list[index]
        else:
            raise ValueError("{}.remove(x):x not in list".format(self.__class__.__name__))

    def remove_every(self,value):
        count=0
        index=self.__bisect_left(value)
        print('begin:{}'.format(index))
        while(index<len(self.__list) and self.__list[index]==value):
            del self.__list[index]
            count +=1
        print(count)
        return count

    def __str__(self):
        return str(list(self.__list))


if __name__=="__main__":
    x=SortedList([1]*2+[2,3,4]+[1]*2,abs)
    x.remove_every(1)
    print(x)
    
