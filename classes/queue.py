class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def __str__(self):
        return str(self.queue)
    def __repr__(self):
        return str(self.queue)
    def __len__(self):
        return len(self.queue)
    def __getitem__(self, index):
        return self.queue[index]
    def __setitem__(self, index, value):
        self.queue[index] = value
    def __delitem__(self, index):
        del self.queue[index]
    def __iter__(self):
        return iter(self.queue)
    def __contains__(self, item):
        return item in self.queue

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)

q.dequeue()

print(q)

print(q[0])

q[0] = 10

print(q)

del q[0]

print(q)

for i in q:
    print(i)

print(1 in q)

print(10 in q)

print(100 in q)

print(len(q))

# Output:
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5]
# 2
# [10, 3, 4, 5]
# [3, 4, 5]
# 3
# 4
# 5
# True
# True
# False
# 3


