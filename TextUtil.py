#!/usr/bin/env python3
"""
This module provides a few string manipulation functions.

>>> is_balanced("(Python (is(not(lisp))))")
True
>>> shorten("The Crossing",10)
'The Cro...'
>>> simplify(" some    text    with  spurious whitespace ")
'some text with spurious whitespace'
>>> is_balanced("][")
False
"""

import string

def shorten(text,length=10,sign='...'):
    if len(text)>length-len(sign):
        return text[:length-len(sign)]+sign
    return text
    
def simplify(text,whitespace=string.whitespace,delete=""):
    word=""
    line=[]
    for char in text:
        if char in whitespace and word=="":
            continue
        elif char in whitespace and word:
            line.append(word)
            word=""
        elif char in delete:
            continue
        else:
            word+=char
    if word:
        line.append(word)
    return " ".join(line)

def is_balanced(text,brackets="()[]{}<>"):
    left_brack=dict.fromkeys(brackets[0::2],0)
    brack_dict=dict(zip(brackets[1::2],brackets[0::2]))
    for char in text:
        if char in brackets[0::2]:
            left_brack[char]+=1
        if char in brackets[1::2]:
            left_brack[brack_dict[char]]-=1
            if left_brack[brack_dict[char]]<0:
                return False
    return not any(left_brack.values())
            
if __name__=="__main__":
    import doctest
    doctest.testmod()
