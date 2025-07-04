from collections import deque

queue = deque()

#enQueue
queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20) #add in rear

print(queue)

#dequeue
queue.popleft() #O(1)
queue.popleft() #remove from front
queue.popleft()
queue.popleft()


#duoble queue
queue.append(9) # add in rear
queue.popleft() # remove from front
queue.appendleft(7) #add in front
queue.pop() #remove from rear

print(queue)


