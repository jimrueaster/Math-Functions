#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: JimruEaster<295140325@qq.com>
# Created on 2017-09-11 16:59


# Get greatest common divisor through Euclidean algorithm
# param int a: an integer
# param int b: another integer
# return int
def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


# Judge the two params are co_prime or not
# param int m: an integer
# param int n: another integer
# return bool
def is_co_prime(m, n):
    return gcd(m,n) == 1


# Get Euler Func
# param int n: an integer
# return int
def get_euler(n):
    cnt = 0
    for i in range(n):
        if is_co_prime(i, n):
            cnt +=1
    return cnt

