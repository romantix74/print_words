#!/usr/bin/env python


""" task 2

 1 1 1   =  1 1 2
 0 0 2   =  0 0 1

3 цифры = 3! =  6 комбинаций
"""


import pytest
import ipdb
import math


@pytest.mark.parametrize("abc, xyz, expected",
                         [((1,1,1),(1,0,2), 10),
                          ((1,2,3),(3,5,4), 28)
                          ])
def test_solution(abc, xyz, expected):
    assert count_combinations(abc,xyz) == expected
    

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(S: list, m: int, n:int ):
  
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1
  
    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0
  
    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        return 0
  
    # count is sum of solutions (i) 
    # including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] )


def count_combinations(abc: tuple, xyz: tuple) -> int:
    # находим общее количество "приведенной" валюты
    
    res = [abc[i]*xyz[i] for i in range(len(abc))]
    print(res)
    
    print(sum(res))
    
    return 10

if __name__ == "__main__":
    # #res = count_combinations((1,2,3),(3,5,4))
    # res = count_combinations((1,1,1),(1,0,2))
    # print(res)
    # fac5 = math.factorial(5)
    # print(fac5/math.factorial())
    
    
    # example 1
    arr_1 = [1,1,1]
    sum_1 = 3
    m_1 = len(arr_1)
    print(f"example_1 {count(arr_1, m_1, sum_1)}")
    
    #arr = [1, 2, 3]
    arr = [1, 2, 3]
    #arr = [1, 0, 2]
    m = len(arr)
    
    for i in range(25 + 1):
        count_of_combinations = count(arr, m, i)
        print(f" for {i} combinations is {count_of_combinations}")