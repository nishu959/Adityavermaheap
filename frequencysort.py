a = list(map(int, input().split()))

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
  heappush(t, (-1*h[i], i))
  
  



while(len(t)>0):
  g =list(heappop(t)) 
  while g[0]!=0:
    print(g[1], end = " ")
    g[0] = g[0] +1
  
  
 