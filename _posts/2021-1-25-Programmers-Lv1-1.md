---
layout: post
title: 프로그래머스 Lv1 추천문제 + 풀이 모음
date:  2021-1-25
author: Jung Jaeeun
categories: Problem-Solving
tags: python coding-test programmers
use_math: true
commtents: true
---

## 추천문제

사실 코딩 수업을 들은 적이 있거나 독학한 적이 있으면 프로그래머스 Lv1은 손쉽게 풀 수 있다. 그리고 그 와중에서도 난이도 차이가 꽤나 많이 나서 추천문제만 모아보았다. 추천 문제들은 주로 구현 문제 또는 엣지 케이스에 잘 걸린다거나 효율성 테스트(시간복잡도 측정)에 걸리는 문제들이다.

- [크레인 인형뽑기 게임](https://programmers.co.kr/learn/courses/30/lessons/64061)
- [신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410)
- [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)
- [2016년](https://programmers.co.kr/learn/courses/30/lessons/12901)
- [3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935)
- [같은 숫자는 싫어](https://programmers.co.kr/learn/courses/30/lessons/12906)
- [문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)
- [소수 찾기](https://programmers.co.kr/learn/courses/30/lessons/12921)
- [시저 암호](https://programmers.co.kr/learn/courses/30/lessons/12926)
- [이상한 문자 만들기](https://programmers.co.kr/learn/courses/30/lessons/12930)
- [키패드 누르기](https://programmers.co.kr/learn/courses/30/lessons/67256)

<br>

## 풀이
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
    tmp = ''
    i = 0
    while i < len(new_id):
        if new_id[i] != '.':
            tmp += new_id[i]
            i += 1
            continue
        j = i
        while j < len(new_id) and new_id[j] == '.':
            j += 1
        i = j
        tmp += '.'
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

### [K번째 수](https://programmers.co.kr/learn/courses/30/lessons/42748)

```python3
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer
```

### [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)

```python3
def solution(n, lost, reserve):
    students = [1] * (n+1)
    # 0번째 학생은 존재하지 않음
    students[0] = 0
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
    for r in reserve:
        # 여벌을 가지고 왔지만 도난당한 경우
        if students[r] == 1:
            continue
        if 1 <= r-1 and students[r-1] == 0:
            students[r-1] += 1
            students[r] -= 1
        elif r+1 <= n and students[r+1] == 0:
            students[r+1] += 1
            students[r] -= 1
    # 여벌을 가지고 왔지만 빌려주지 못한 경우를 위해 min 함수 적용
    students = [min(1, st) for st in students]
    return sum(students)
```

생각보다 신경써야 할 케이스가 많아서 푸는데 시간이 좀 걸렸다.

### [2016년](https://programmers.co.kr/learn/courses/30/lessons/12901)

```python3
def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 월, 일, 요일
    month = day = 1
    now = 5
    while month != a or day != b:
        now = (now + 1) % len(days)
        day += 1
        # 한 달이 지나면
        if day > months[month]:
            day = 1
            month += 1 
    answer = days[now]
    return answer
```

요일에 해당하는 배열과 각 달의 일수를 저장한 배열을 이용하면 어렵지 않은 문제였다.

### [가운데 글자 가져오기](https://programmers.co.kr/learn/courses/30/lessons/12903)

```python3
def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2-1] + s[len(s)//2]
    return answer
```

### [3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935)

```python3
def solution(n):
    triple = ''
    while n >= 1:
        triple += str(n % 3)
        n //= 3

    i = len(triple)-1
    d = 1
    answer = 0
    while i >= 0:
        answer += int(triple[i]) * d
        d *= 3
        i -= 1
    return answer
```

```triple```을 만들 때 이미 뒤집어져있으므로 바로 10진법으로 바꿔주면 된다.

### [같은 숫자는 싫어](https://programmers.co.kr/learn/courses/30/lessons/12906)

```python3
def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        j = i
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        answer.append(arr[i])
        i = j
    return answer
```

슬라이딩 윈도우를 이용하여 풀어주었다.

### [나누어 떨어지는 숫자 배열](https://programmers.co.kr/learn/courses/30/lessons/12910)

```python3
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    if not answer:
        answer = [-1]
    answer.sort()
    return answer
```

### [두 정수 사이의 합](https://programmers.co.kr/learn/courses/30/lessons/12912)

```python3
def solution(a, b):
    a, b = min(a, b), max(a, b)
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer
```

### [문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)

```python3
def solution(strings, n):
    answer = sorted(strings)
    answer = sorted(answer, key=lambda x: x[n])
    return answer
```

쉬운 문제지만 인덱스 n으로 정렬하는 것이 사전순정렬보다 우선순위이기 때문에 **직관과 반대로 먼저 사전순정렬을 해준 다음에 인덱스 n으로 정렬해야 한다.**

### [문자열 내 p와 y의 개수](https://programmers.co.kr/learn/courses/30/lessons/12916)

```python3
def solution(s):
    s = s.lower()
    p_num = y_num = 0
    for ch in s:
        if ch == 'p':
            p_num += 1
        elif ch == 'y':
            y_num += 1
    return p_num == y_num
```

### [문자열 내림차순으로 배치하기](https://programmers.co.kr/learn/courses/30/lessons/12917)

```python3
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    answer = ''.join(s)
    return answer
```

### [문자열 다루기 기본](https://programmers.co.kr/learn/courses/30/lessons/12918)

```python3
def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    for ch in s:
        if not ch.isdigit():
            return False
    return True
```

파이썬 string의 내장 메소드인 ```isdigit()```을 활용하면 더 쉽게 풀 수 있는 문제였다.

### [서울에서 김서방 찾기](https://programmers.co.kr/learn/courses/30/lessons/12919)

```python3
def solution(seoul):
    idx = seoul.
    answer = "김서방은 " + str(idx) + "에 있다"
    return answer
```

### [소수 찾기](https://programmers.co.kr/learn/courses/30/lessons/12921)

(틀린 코드)
```python3
def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_prime(i):
            answer += 1
    return answer

def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
```

이 문제는 일반적인 소수를 찾는 방법을 주어진 범위에 모두 적용하면 효율성 테스트에서 틀린다ㅠㅠ 따라서 보다 효율적인 알고리즘을 사용해야하는데, <strong>[에라토스테네스의 체](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4#%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4%EB%A5%BC_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4%EB%A1%9C_%EA%B5%AC%ED%98%84)</strong>라는 알고리즘을 사용하면 된다.

(맞는 코드)
```python3
def solution(n):
    array = [True] * (n+1)
    # 0과 1은 소수가 아니다.
    array[:2] = [False] * 2
    i = 2
    while i*i <=  n:
        if array[i]:
            j = 2*i
            while j <= n:
                array[j] = False
                j += i
        i += 1
    answer = sum(array)
    return answer
```

### [수박수박수박수박수박수?](https://programmers.co.kr/learn/courses/30/lessons/12922)

```python3
def solution(n):
    answer = ''
    arr = ['수', '박']
    for i in range(n):
        answer += arr[i % 2]
    return answer
```

### [문자열을 정수로 바꾸기](https://programmers.co.kr/learn/courses/30/lessons/12925)

```python3
def solution(s):
    return int(s)
```

역시 코테는 파이썬이 짱인듯하다..

### [내적](https://programmers.co.kr/learn/courses/30/lessons/70128)

```python3
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
```

### [시저 암호](https://programmers.co.kr/learn/courses/30/lessons/12926)

```python3
def solution(s, n):
    answer = ''
    for ch in s:
        if ch == ' ':
            answer += ch
        # 소문자라면
        elif ord('a') <= ord(ch) <= ord('z'):
            tmp = ord(ch)+n
            if tmp > ord('z'):
                tmp -= 26
            answer += chr(tmp)
        # 대문자라면
        else:
            tmp = ord(ch)+n
            if tmp > ord('Z'):
                tmp -= 26
            answer += chr(tmp)
    return answer
```

'z' 같은 경우에는 1을 더했을 때 'a'가 나와야 하므로 'z'보다 크면 26을 빼줘야하는게 이 문제의 핵심이었다.

### [약수의 합](https://programmers.co.kr/learn/courses/30/lessons/12928)

```python3
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer
```

### [이상한 문자 만들기](https://programmers.co.kr/learn/courses/30/lessons/12930)

```python3
def solution(s):
    answer = ''
    i = 0
    for ch in s:
        if ch == ' ':
            answer += ch
            i  = 0
            continue
        if i % 2 == 0:
            answer += ch.upper()
        else:
            answer += ch.lower()
        i += 1
    return answer
```

공백을 기준으로 단어를 분리해서 짝/홀수를 세어줘야 하기 때문에 공백을 만나면 ```i=0```이 된다.

### [자릿 수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931)

```python3
def solution(n):
    answer = 0
    string = str(n)
    for ch in string:
        answer += int(ch)
    return answer
```

### [자연수 뒤집어 배열로 만들기](https://programmers.co.kr/learn/courses/30/lessons/12932)

```python3
def solution(n):
    string = str(n)[::-1]
    answer = []
    for ch in string:
        answer.append(int(ch))
    return answer
```

### [정수 내림차순으로 배치하기](https://programmers.co.kr/learn/courses/30/lessons/12933)

```python3
def solution(n):
    answer = 0
    lst = list(str(n))
    lst.sort(reverse=True)
    answer = int(''.join(lst))
    return answer
```

### [정수 제곱근 판별](https://programmers.co.kr/learn/courses/30/lessons/12934)

```python3
def solution(n):
    i = 1
    x = -1
    while i*i <= n:
        if i*i == n:
            x = i
        i += 1
        
    if x == -1:
        answer = -1
    else:
        answer = (x+1) ** 2
    return answer
```

### [제일 작은 수 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12935)

```python3
def solution(arr):
    min_val = min(arr)
    answer = [x for x in arr if x != min_val]
    if not answer:
        answer.append(-1)
    return answer
```

### [짝수와 홀수](https://programmers.co.kr/learn/courses/30/lessons/12937)

```python3
def solution(num):
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer
```

### [키패드 누르기](https://programmers.co.kr/learn/courses/30/lessons/67256)

```python3
def solution(numbers, hand):
    answer = ''
    # 왼손, 오른손 위치
    l = (3, 0)
    r = (3, 2)
    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            l = n//3, 0
        elif n in (3, 6, 9):
            answer += 'R'
            r = n//3-1, 2
        else:
            c = (n//3, 1)
            # 0인 경우 예외 처리
            if n == 0:
                c = (3, 1)
            l_dist = distance(l, c)
            r_dist = distance(r, c)
            if l_dist < r_dist:
                l = c
                answer += 'L'
            elif r_dist < l_dist:
                r = c
                answer += 'R'
            else: # 두 거리가 같을때
                if hand == 'left':
                    answer += 'L'
                    l = c
                else:
                    answer += 'R'
                    r = c
    return answer

def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
```

```numbers```안에 있는 0을 따로 예외처리해줘야 한다. 그 부분만 빼면 평범한 구현문제인듯하다.