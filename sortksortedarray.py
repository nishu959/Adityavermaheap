from heapq import heappop, heappush, heapify

a = list(map(int, input().split()))
k = int(input())

t = []
heapify(t)

for i in a:
  heappush(t, i)
  if len(t)>k:
    print(heappop(t),end = " ")  

while t:   
    print(heappop(t), end= " ")
