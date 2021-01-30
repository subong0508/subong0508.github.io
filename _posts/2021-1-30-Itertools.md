---
layout: post
title: Itertools 정리
date:  2021-1-30
author: Jung Jaeeun
categories: Python
tags: python coding-test
use_math: true
commtents: true
---

내장 라이브러리인 ```itertools```를 이용해서 조합, 순열, 중복순열, Cartesian Product 등을 손쉽게 구현할 수 있다.

```python3
from itertools import combinations, permutations, combinations_with_replacement, product

data = '123'
l = combinations(data, 2)
for e in l:
    print(*e) # 12 13 23

l = permutations(data, 2)
for e in l:
    print(*e) # 12 13 21 23 31 32

l = combinations_with_replacement(data, 2)
for e in l:
    print(*e) # 11 12 13 22 23 33

l = product(data, repeat=2)
for e in l:
    print(*e) # 11 12 13 21 22 23 31 32 33
```