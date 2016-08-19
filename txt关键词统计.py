class FileCount:
    def __init__(self,path):
        self.file=open(path,encoding='utf-8')
    def word_count(self,words,people=None):
        total={}.fromkeys(words,0)
        for line in self.file:
            for word in total.keys():
                if word in line:
                    #print('{} in {}'.format(word,line))
                    total[word]+=line.count(word)
        self.file.close()
        total_list=[(key,value) for key,value in total.items()]
        total_list.sort(key=lambda x:x[1],reverse=True)
        for key,value in total_list:
            print('{0:<{2}}:{1}'.format(key,value,11-len(key)))
        #如果输入人员分类，则输出人员出场统计
        if people:
            print("="*30)
            people_dic={}.fromkeys(people.keys(),0)
            for name,alias in people.items():
                summary=0
                for key in total:
                    if key in alias:
                        summary += total[key]
                people_dic[name]=summary
            people_list=[(key,value) for key,value in people_dic.items()]
            people_list.sort(key=lambda x:x[1],reverse=True)
            for key,value in people_list:
                print('{0:<{2}}出现次数{1}'.format(key,value,8-len(key)))
            
                
        


f = FileCount('4447.txt')
words=['美猴王','猴王','孙悟空','悟空','大圣','孙行者','行者','孙大圣','弼马温',
       '玄奘','三藏','唐僧','圣僧',
       '悟能','八戒','天篷',
       '沙僧','悟净','沙和尚']
people={'孙悟空':['美猴王','猴王','孙悟空','悟空','大圣','孙行者','行者','孙大圣','弼马温'],
        '唐僧':['玄奘','三藏','唐僧','圣僧'],
        '猪八戒':['悟能','八戒','天篷'],
        '沙和尚':['沙僧','悟净','沙和尚']}
f.word_count(words,people)

