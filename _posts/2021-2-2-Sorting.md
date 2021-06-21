---
layout: post
title: 정렬 with Python
date:  2021-2-2
author: Jung Jaeeun
category: Data structure
tags: sorting python data-structure
use_math: true
commtents: true
---

이번 포스팅에서는 여러 정렬 기법에 대해 알아보고 파이썬으로 간단하게 구현해보겠습니다.

## 선택 정렬(Selection Sort)

선택 정렬은 한마디로 **Priority Queue with Unsorted Array**라고 할 수 있습니다.
우선순위 큐가 하나 있다고 가정해봅시다. 데이터를 삽입할 때는 항상 끝에 삽입하고, 
```pop``` 연산을 오름차순/내림차순으로 수행합니다. 또한 시간복잡도는 $O(n^2)$ 입니다.

```python3
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # swap
    array[min_idx], array[i] = array[i], array[min_idx]

print(array)
```

## 삽입 정렬(Insertion Sort)

삽입 정렬은 선택 정렬과 반대로 **Sorted Array**로 구현된 우선순위 큐입니다. 최악의 경우 시간복잡도는 선택 정렬과 동일하게 $O(n^2)$이지만 이미 정렬된 경우에는 $O(n)$에 가까울 정도로 빠릅니다. 

```python3
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)-1):
    j = i+1
    while j >= 1 and array[j] < array[j-1]:
        # swap
        array[j-1], array[j] = array[j], array[j-1]
        j -= 1

print(array)
```

## 힙 정렬(Heap Sort)

힙 정렬은 이름과 같이 힙을 이용하여 정렬하는 방법입니다. 시간복잡도는 $O(n\log n)$에 해당합니다.

```python3
import heapq

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def heap_sort(arr):
    q = []
    for a in arr:
        heapq.heappush(q, a)
    arr = []
    while q:
        arr.append(heapq.heappop(q))
    return arr

print(heap_sort(array))
```

## 퀵 솔트(Quick Sort)

퀵 솔트란 하나의 피봇을 정해서 피봇보다 작은 값들 - 피봇 - 피봇보다 큰 값들 순으로 오도록 하는 알고리즘입니다. 퀵 솔트의 구현에서는 대부분 재귀함수를 사용합니다. 시간 복잡도는 보통 $O(n \log n)$이지만 최악의 경우엔 $O(n^2)$이 되기도 합니다.

```python3
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    array = array[1:]

    left_partition = [x for x in array if x <= pivot]
    right_partition = [x for x in array if x > pivot]

    return quick_sort(left_partition) + [pivot] + quick_sort(right_partition)

print(quick_sort(array))
```

## 합병 정렬(Merge Sort)

마지막으로 살펴볼 정렬 기법은 합병 정렬입니다. 합병 정렬은 어떤 경우에도 $O(n \log n)$의 성능을 보장하지만 대부분의 경우에 퀵 정렬보다 느리다고 합니다. 또한 합병 정렬은 **Divide and Conquer**의 대표적인 알고리즘 중 하나입니다.

```python3
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def merge(lst1, lst2):
    n1, n2 = len(lst1), len(lst2)
    i = j = 0
    lst = []
    while i < n1 and j < n2:
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1

    while i < n1:
        lst.append(lst1[i])
        i += 1
    
    while j < n2:
        lst.append(lst2[j])
        j += 1

    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort(array))
```