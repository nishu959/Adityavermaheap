from heapq import heappop, heappush, heapify 

def ksn(a, k):
  t = []
  heapify(t)
  
  for i in a:
    heappush(t, -1*i)
    if len(t)>k:
      heappop(t)     
  
  return -1*heappop(t)


a = list(map(int, input().split()))
k1 = int(input())
k2 = int(input())

m=ksn(a, k1)
n=ksn(a, k2)
s = 0
for i in a:
  if i>m and i<n:
    s = s+i
       
print(s)
    