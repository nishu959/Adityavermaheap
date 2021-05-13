from heapq import heappop, heappush, heapify

a = list(map(int, input().split()))
k = int(input())
x = int(input()) 
#how to push pair in heap
#heappush(h, (7, 'release product'))
t = [] 
heapify(t)
for i in a:
  heappush(t, (-1*abs(x-i),i)) 
  if len(t)>k:
    heappop(t)
    

for i, j in t:
  print(j, end= " ")
  
