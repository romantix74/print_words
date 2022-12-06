#!/usr/bin/env python

"""_summary_
    Ксюша недавно устроилась работать в Тинькофф. В качестве первого задания ей поручили выбрать цвета для названия нового отдела. 
    Ксюша уже решила, что покрасит его в два цвета — желтый и черный, осталось только раскрасить. 

    Название отдела представляет из себя строку ss, состоящую из нескольких слов, разделенных пробелами. 
    Каждое слово состоит из латинских букв, суммарно в названии их ровно nn.  
    
    Ксюша уже придумала, в какие цвета покрасит каждую букву, но хочет, чтобы раскраска получилась наиболее красивой. 
    Слово считается некрасивым, если в нем есть соседние буквы, покрашенные в один цвет.  

    Ксюша хочет узнать, сколько слов в названии отдела окажутся некрасивыми, если раскрашивать их в соответствии с ее идеей. 
    Пожалуйста, помогите ей сосчитать. 


    Формат входных данных 
    
    В первой строке вводится число nn (1 ≤ n ≤ 100)(1≤n≤100) — количество букв в названии отдела. 
    
    Во второй строке вводится само название — строка ss (1 ≤ |s| ≤ 100)(1≤ ∣s∣ ≤100), состоящая из латинских букв и пробелов. 
    Гарантируется, что между любыми двумя буквами не более одного пробела, строка начинается и заканчивается буквой, 
    а также содержит ровно nn букв. 
    
    В третьей строке вводится строка bb длины nn, состоящая из букв YY и BB  — Ксюшина идея раскраски названия. Если b_i = Yb  
    i 

    =Y, то ii-ая по счету буква названия должна быть покрашена в желтый цвет; если же b_i = Bb  
    i 

    =B, то ii-ая буква должна быть покрашена в черный цвет. 
    

    Формат выходных данных 
    
    В единственной строке выведите число — количество некрасивых слов в раскрашенном названии отдела.
"""

import pytest
import ipdb

@pytest.mark.parametrize("nn,ss,bb, expected",
                         [(7,'Tynkoff','BYBYBYB', 0),
                          (8,'Tyn word','BYBBYBYB', 0),
                          (8,'Tyn word','BBBBYBYB', 1),
                          (8,'Ty wo rd','BYBBYBYB', 0),
                          (8,'Ty wo rd','BYBBBBBB', 2)])
def test_solution(nn,ss,bb, expected):
    assert print_words(nn,ss,bb) == expected


def print_words(nn: int, ss: str, bb: str) -> int:
    
    # счетчик некрасивых слов
    counter_bad_words = 0
    
    words = ss.split(" ")
    print(words)
    
    # составляем соттвествуйщие слова цветов
    color_words_list = []
    
    index = 0
    for word in words:
        color_word = bb[index:len(word)+index]
        color_words_list.append(color_word)
        index = len(word)+1
     

    print(color_words_list)

    #cnt = [ counter+=1 for i in color_words_list if (("BB" in i) or ("YY" in i)) ]

    for i in color_words_list:
        if (("BB" in i) or ("YY" in i)):
            counter_bad_words += 1
    
    print(counter_bad_words)
    
    return counter_bad_words
    
    # находим индексы пробелов
    # import ipdb; ipdb.set_trace()
    
    
    # if ' ' in ss:
        
    #     #print(ss.index(' '))
        
    #     # строка, соответствуюшая текущему слову
    #     current_word = ""
    #     for i in range(nn):
    #         print(f"{ss[i]} {bb[i]}")
            
            
    #         #  слово отделенное пробелом или последнее слово
    #         if ' ' == ss[i] or i == nn-1:
    #             #import ipdb; ipdb.set_trace() 
    #             if ("BB" in current_word) or ("YY" in current_word):
    #                 counter_bad_words += 1 
    #                 print("+ bad word")
    #             current_word = ""   
    #             print("\n")  
    #         else:            
    #             current_word += bb[i]
    #         print(current_word)
                    
    #     print(counter_bad_words)
    #     return counter_bad_words
            
    # если только одно слово 
    # else:
    #     if ("BB" in ss) or ("YY" in ss):
    #         return 1
    #     # одно слово и оно красивое
    #     else:
    #         return 0

if __name__ == "__main__":
    #print_words(8,'Tyn word','BBBBYBYB')
    #print_words(8,'Ty wo rd','BYBBBBBB')
    print_words(8,'Ty wo rd','BYBBYBYB')
    #print_words(7,'Tynword','BBBBBYB')
    #print_words(7,'Tynword','BYBYBYB')
    #print_words(7,'Algorithms and Data Structures','BBBBBBBBBBBYBYYYYBBBBBBBBB')
    
    
    #print("\n")
    