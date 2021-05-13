a = list(map(int, input().split()))
k = int(input())
h = {}
for i in a:
  if i in h:
    h[i] = h[i]+1
  else:
    h[i] = 1
  
from heapq import heappop, heappush, heapify
t = []
heapify(t)
for i in h:
  heappush(t, (h[i], i))
  if len(t)>k:
    heappop(t)


for i, j in t:
  print(j, end= " ")