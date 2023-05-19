def create_queue():
    queue = []
    return queue


def is_empty(queue):
    if len(queue) == 0:
        return True


def enqueue(queue, data):
    queue.insert(0, data)
    return True

queue1 = create_queue()
enqueue(queue1, 0)
enqueue(queue1, 1)
enqueue(queue1, 2)
enqueue(queue1, 3)

print(queue1)