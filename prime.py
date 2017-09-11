#!/usr/bin/python3

# -*- coding:utf-8 -*-

from math import sqrt


def is_prime(n):
    if 0 not in [n%i for i in range(2, int(sqrt(n))+1)]:
        return True
    else:
        return False


def get_prime(min_num, max_num, reverse=False):
    lst = []
    min_num = int(min_num)
    max_num = int(max_num)+1
    candidate_range = range(min_num, max_num)

    if reverse is True:
        candidate_range = range(max_num, min_num, -1)

    for n in candidate_range:
        if n == 1:
            continue
        elif n == 2:
            lst.append(2)
        else:
            if 0 not in [n % i for i in range(2, int(sqrt(n)))]:
                lst.append(n)
    return lst