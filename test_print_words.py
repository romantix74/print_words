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
                          (8,'Ty wo rd','BYBBYBYB', 1),
                          (8,'Ty wo rd','BYBBBBBB', 2),
                          (11,'Наш общий дом', 'YBYYYBBYYBY', 1)])
def test_solution(nn,ss,bb, expected):
    assert print_words(nn,ss,bb) == expected


def print_words(nn: int, ss: str, bb: str) -> int:
    
    # счетчик некрасивых слов
    counter_bad_words = 0
    
    words = ss.split(" ")
    print(words)
    
    # составляем соответствующие слова цветов
    color_words_list = []
    
    index = 0
    for word in words:
        color_word = bb[index:len(word)+index]
        color_words_list.append(color_word)
        index = len(word) + index  # + 1  # 1 это для пробела
     

    print(color_words_list)

    counter_bad_words = len([ i for i in color_words_list if (("BB" in i) or ("YY" in i)) ])
    # print(f"cnt = {counter_bad_words} and len in {len(counter_bad_words)}")

    # for i in color_words_list:
    #     if (("BB" in i) or ("YY" in i)):
    #         counter_bad_words += 1
    
    #print(counter_bad_words)
    
    return counter_bad_words
    
 
if __name__ == "__main__":
    #print_words(8,'Tyn word','BBBBYBYB')
    #print_words(8,'Ty wo rd','BYBBBBBB')
    #print_words(8,'Ty wo rd','BYBBYBYB')
    #print_words(7,'Tynword','BBBBBYB')
    #print_words(7,'Tynword','BYBYBYB')
    print_words(27,'Algorithms and Data Structures','BBBBBBBBBBBYBYYYYBBBBBBBBB')
    print_words(11,'Наш общий дом', 'YBYYYBBYYBY' )
    
    
    #print("\n")
    