---
layout: post
title: 프로그래머스 Lv1 풀이 모음
date:  2021-1-25
author: Jung Jaeeun
categories: Problem-Solving
tags: python coding-test programmers
use_math: true
commtents: true
---

### [크레인 인형뽑기 게임](https://programmers.co.kr/learn/courses/30/lessons/64061)

```python3
def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0:
                stack.append(board[i][m-1])
                board[i][m-1] = 0
                # 인형삭제
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer
```

### [두 개 뽑아서 더하기](https://programmers.co.kr/learn/courses/30/lessons/68644)

```python3
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer = sorted(answer)
    return answer
```

set 자료형으로 중복된 값이 삽입되지 않게 구현하였다. 시간복잡도는 $n^2 + n\log n \rightarrow O(n^2)$

### [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576)

```python3
def solution(participant, completion):
    d = {}
    for p in participant:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    
    for c in completion:
        d[c] -= 1
    
    for k in d:
        if d[k] != 0:
            answer = k
            break
    return answer
```

dictionary 자료형을 이용해서 돔영이인도 처리해주었음. 시간복잡도는 $3n \rightarrow O(n)$

### [신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410)

```python3
import string

def solution(new_id):
    # 1. 대문자->소문자
    new_id = new_id.lower()
    # 2. 유효하지 않은 문자 제거
    valid_str = list(string.ascii_lowercase) + list(map(str, range(10))) + ['-', '_', '.']
    valid_str = set(valid_str)
    tmp = ''
    for i in range(len(new_id)):
        # O(1)
        if new_id[i] in valid_str:
            tmp += new_id[i]
    new_id = tmp
    # 3. 마침표 두 번 치환
    tmp = new_id
    for i in range(len(new_id)):
        if new_id[i] != '.':
            continue
        j = i
        cnt = 0
        while j < len(new_id) and new_id[j] == '.':
            j += 1
            cnt += 1
        tmp = tmp.replace('.' * cnt, '.')
    new_id = tmp
    # 4. 처음이나 끝 '.' 제거
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5. 빈 문자열이라면 'a' 대입
    if new_id == '':
        new_id = 'a'
    # 6. 길이가 16자 이상이라면 15개까지만
    if len(new_id) >= 16:
        new_id = new_id[:15]
        # 마지막 '.' 처리
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 길이가 2자 이하라면
    if len(new_id) <= 2:
        ch = new_id[-1]
        while len(new_id) < 3:
            new_id += ch
    return new_id
```

3번에서 마침표가 여러번 나오는 걸 하나의 마침표로 치환해주는게 조금 복잡해서 애먹은 문제..

### [모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840)

```python3
def solution(answers):
    answer = []
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = get_cnt(st1, answers)
    cnt2 = get_cnt(st2, answers)
    cnt3 = get_cnt(st3, answers)
    cnts = [cnt1, cnt2, cnt3]
    max_val = max(cnts)
    for i in range(3):
        if cnts[i] == max_val:
            answer.append(i+1)
    return answer

def get_cnt(st, answers):
    cnt = 0
    for i in range(len(answers)):
        if st[i % len(st)] == answers[i]:
            cnt += 1
    return cnt
```