---
layout: post
title: Graph Theory with Python
date:  2021-2-28
author: Jung Jaeeun
categories: Data-Structure
tags: python data-structure graph shortest-path
use_math: true
commtents: true
---

# 서로소 집합

**시간복잡도: $O(V + M \log_{2}{V})$**

```python3
# 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 merge
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
```

**사이클 판별**

```python3
for i in range(num_edges):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print("Cycle")
    else:
        union(parent, a, b)
```

# 크루스칼 알고리즘: Minimum Spanning Tree

**시간복잡도: $O(E \log {E})$**

```python3
res = 0
edges.sort()
for e in edges:
    cost, a, b = e
    # not cycle
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        res += cost
```

# 위상 정렬

**시간복잡도: $O(V + E)$**

```python3
def topological_sort():
    result = []
    q = deque()

    # 진입차수가 0인 노드들 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수가 0이 된다면
            if indegree[i] == 0:
                q.append(i)
    
    return result
``` 