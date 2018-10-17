import pytest
import random

random.seed(10)

def gcd(m: int, n: int) -> int:
    """
    Реализация бинарного алгоритма вычисления наибольшего общего делителя

    :param m:
    :param n:
    :return:
    """
    if m == 0 and n != 0:
        return n
    
    if n == 0 and m != 0:
        return m
    
    if m == n:
        return m
    
    if n == 1 or m == 1:
        return 1

    if m % 2 == 0 and n % 2 == 0:
        return 2 * gcd(m // 2, n // 2)

    if m % 2 == 0 and n % 2 == 1:
        return gcd(m // 2, n)

    if m % 2 == 1 and n % 2 == 0:
        return gcd(n, m // 2)

    m, n = max(m, n), min(m, n)
    return gcd((m - n) // 2, n)
'''
print('print:')
test = gcd(m = int(input("first: ")),n=int(input("second: ")))
print(test)
'''

def test_equal():
    assert gcd(5,5) == 5

def test_zero():
    assert gcd(0,6) == 6
    assert gcd(6,0) == 6

def test_string():
    assert gcd("4","2") == 2

def test_negative():
    assert gcd(-4,-2) == -2

def test_one():
    assert gcd(4,1) == 1
    assert gcd(1,1) == 1

def test_even():
    assert gcd(8,16) == 8
    assert gcd(8,14) == 2

def test_odd():
    assert gcd(7,9) == 1
    assert gcd(6,3) == 3

def test_mixed():
    assert gcd(21,6) == 3

def test_random():
    key = random.randint(3,6)
    m = 3*key
    n = 4*key
    assert gcd(m,n) == key

def test_big():
    assert gcd(100000,20000) == 20000


#py.test -s "/home/ivannd/Git/python-solution/Solution Lesson 4/gcd.py"