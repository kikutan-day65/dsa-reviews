class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    