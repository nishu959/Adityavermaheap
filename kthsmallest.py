from heapq import heappop, heappush, heapify
#There is no max heap in python
#so we push every element by changing it sign
# by multiplying it with -1
#At last we return the top element
# by multiplying with - 1
# in [1,2,5,3,6] = 4th smallest = 5
#now in [-1,-2,-5,-3,-6] ,4th greatest = -5 
#for ans = 5 *-1= 5

a = list(map(int, input().split()))
k = int(input())

t = []
heapify(t)

for i in a:
  heappush(t, -1*i)
  if len(t)>3:
    heappop(t) 
print(t[0] * -1)
