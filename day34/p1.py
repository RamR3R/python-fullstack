from collections import deque
ppl = ["Ram" , "Sam" , "Jas" , "Bas" , "Mar"]
waiting_time = [4, 1, 5, 6, 3]
time = 1

queue = deque(ppl)
waiting_time_queue = deque(waiting_time)

while len(queue) != 0:
    guy = queue.popleft()
    if waiting_time_queue.popleft() > time:
        print(f"{guy} got the ticket at time :" , time)
    else:
        print(f"{guy} left out of frustration at :" , time)
    time += 1



