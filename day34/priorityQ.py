#priority Queue

import heapq

priorQ = []

#enqueue in PQ
heapq.heappush(priorQ , 5)  #add to PQ
print(priorQ)
heapq.heappush(priorQ , 1)
print(priorQ)
heapq.heappush(priorQ , 2)
print(priorQ)
heapq.heappush(priorQ , 3)
print(priorQ)
heapq.heappush(priorQ , 0)
print(priorQ)

#dqueue operation
heapq.heappop(priorQ)
print(priorQ)

while priorQ:
    print(heapq.heappop(priorQ))

# print("front element : ",priorQ[0]) #peek function

