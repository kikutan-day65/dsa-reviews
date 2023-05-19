def create_queue():
    queue = []
    return queue


def is_empty(queue):
    if len(queue) == 0:
        return True


def enqueue(queue, data):
    queue.insert(0, data)
    return True


def dequeue(queue):
    queue.pop()
    return True

queue1 = create_queue()
enqueue(queue1, 0)
enqueue(queue1, 1)
enqueue(queue1, 2)
enqueue(queue1, 3)

print(queue1)

queue2 = create_queue()
enqueue(queue2, 0)
enqueue(queue2, 1)
enqueue(queue2, 2)
enqueue(queue2, 3)
dequeue(queue2)

print(queue2)