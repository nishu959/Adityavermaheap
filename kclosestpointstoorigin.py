from heapq import heappop, heappush, heapify 
a = []

#here one input for no of points in 2 d array
N = int(input())
for i in range(N):
  m, n = map(int, input().split())
  a.append((m, n)) 
  
k = int(input())


t = [] 
heapify(t)

for i in a:
  i = list(i)
  heappush(t, (-1 * (i[0]**2+i[1]**2),(i[0],i[1])))
  if len(t)>k:
    heappop(t)
    

for i, j in t:
  print(j, end= " ")
  