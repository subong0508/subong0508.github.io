---
layout: post
title: Shortest Path with Python
date:  2021-2-27
author: Jung Jaeeun
categories: Data-Structure
tags: python data-structure graph shortest-path
use_math: true
commtents: true
---

오늘은 파이썬을 이용해 weighted graph(가중치가 있는 그래프)에서 최단 경로를 찾는 방법을 알아보겠습니다.

가중치가 없는 그래프라면 **BFS**를 통해 최단 경로를 손쉽게 구할 수 있습니다.

# 다익스트라 알고리즘

다익스트라 알고리즘은 한 노드에서 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘입니다.
다익스트라는 기본적으로 그리디 알고리즘의 한 종류로, 방문하지 않은 노드 중 가장 가까운 노드를 통해 갈 수 있는 경로를 개선합니다.

다익스트라 알고리즘을 사용할 때는 시간복잡도를 개선하기 위해 힙 자료구조를 사용하고, 시간 복잡도는 $O(E \log {V})$가 됩니다. 

파이썬으로 간단하게 구현하면 다음과 같습니다.

```python3
import heapq


# weighted graph
graph = [
    [0, 10, 20],
    [2, 0, 3],
    [10, 4, 0]
]
INF = int(1e9)


def dijkstra(start, graph):
    distance = [INF for _ in range(len(graph))]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start)) # 거리, 노드
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드
        if distance[now] < dist:
            continue
        for i in range(len(graph)):
            if dist+graph[now][i] < distance[i]:
                distance[i] = dist+graph[now][i]
                heapq.heappush(q, (distance[i], i))
    return distance


print(dijkstra(0, graph)) # 0 10 13
print(dijkstra(1, graph)) # 2 0 3
print(dijkstra(2, graph)) # 6 4 0
```

# 플로이드 워셜 알고리즘

다음은 모든 지점에서 다른 모든 지점으로 가는 최단 경로를 구해주는 플로이드 워셜 알고리즘에 대해서 알아보겠습니다.

플로이드 워셜 알고리즘의 시간복잡도는 $O(V^{3})$이라, 일반적인 코딩 테스트 환경에서는 정점의 수가 1000개 이하인 경우만 가능합니다.

파이썬으로 구현한 코드는 다음과 같습니다.

```python3
# weighted graph
INF = int(1e9)
graph = [
    [0, 4, INF, 6],
    [3, 0, 7, INF],
    [5, INF, 0, 4],
    [INF, INF, 2, 0]
]
n = len(graph)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

print(*graph, sep='\n')
```