from heapq import heappop, heappush, heapify 
a = list(map(int, input().split()))

cost = 0
t = []
heapify(t)

for i in a:
  heappush(t, i)
 
while(len(t)>=2):
  p = heappop(t)
  q = heappop(t)
  cost = cost + p +q
  heappush(t, p+q)
  
  
print(cost)
  