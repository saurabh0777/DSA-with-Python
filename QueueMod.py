from queue import Queue

q = Queue()
q.put(10)
q.put(20)
print(q.queue)

q.get()

print(q.queue)
