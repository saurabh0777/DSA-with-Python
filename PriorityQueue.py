# Lowest element based priority

Q = []
Q.append(10)
Q.append(20)
Q.append(5)

print(Q)

q = sorted(Q)

print(q)
print(q.pop(0))
print(q)

from queue import PriorityQueue
a = PriorityQueue()
a.put(10)
a.put(20)
a.put(4)

print(a.queue)

