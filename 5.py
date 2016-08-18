import sys
import unicodedata

def print_unicode_table(word):
    print("decimal hex chr {0:^40}".format("name"))
    print("------- --- --- {0:-<40}".format(""))
    code=ord(" ")
    end=sys.maxunicode

    while code<ord(" ")+20:
        c=chr(code)
        name=unicodedata.name(c,"*** unknow ***")
        if word is None or word in name.lower():
            print("{0:^7}  {0:<2X} {0:^3c} {1}".format(code,name.title()))
        code +=1

word=input("请输入关键字:")
if word in ('-h','--help'):
    print("输入关键字，查询对应的unicode字符")
    word=0
else:
    word=word.lower()
if word!=0:
    print_unicode_table(word)
    
    

