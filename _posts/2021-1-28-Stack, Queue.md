---
layout: post
title: 스택, 큐 with Python
date:  2021-1-28
author: Jung Jaeeun
categories: Data-Structure
tags: python coding-test programmers boj baekjoon
use_math: true
commtents: true
---

이번 포스팅에서는 스택, 큐에 대한 개념을 알아보고 파이썬으로 간단하게 구현해보겠습니다.

# 스택

스택은 **LIFO**(후입선출)의 특성을 가진 자료구조입니다. 시간복잡도는 다음과 같습니다.

- 삽입: $O(1)$
- 삭제: $O(1)$

파이썬에서는 다른 라이브러리를 쓸 필요없이 기본 자료형인 ```list```를 활용하여 삽입 및 삭제 연산을 수행할 수 있습니다.

```python3
arr = [1, 2, 3, 4, 5]
stack = []

# 삽입
for a in arr:
    stack.append(a)
print(stack)

# 삭제
while stack:
    print(stack.pop())
```

# 큐

큐는 기본적으로 **FIFO**(선입선출)의 특성을 띄는 자료구조입니다. 시간복잡도는 앞서 설명한 스택과 동일합니다.

주의해야할 점은 스택과 다르게 파이썬의 기본 자료구조인 ```list```를 사용해서 ```pop(0)```을 통해 삭제연산을 수행하면 시간복잡도가 $O(n)$이 된다는 것입니다. 

따라서 ```list```를 쓰기보다는 파이썬에서는 내장 모듈인 ```collections```의 ```deque```을 쓰면 간단하게 구현할 수 있습니다. 

```python3
from collections import deque

q = deque()

# 삽입
arr = [1, 2, 3, 4, 5]
for a in arr:
    q.append(a)

# peek
print(q[0])

# pop
# popleft 말고 pop을 쓰면 선입선출
while q:
    print(q.popleft())
```