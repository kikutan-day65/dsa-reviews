class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    #=====================================

    def print_list(self):
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
    
    #=====================================

    def is_empty(self):
        if self.front == None:
            return True
        return False
    
    #=====================================

    def enqueue(self, data):
        new_node = QueueNode(data)
        temp = self.front
        new_node.next = temp
        self.front = new_node

        return True


queue1 = Queue()
queue1.enqueue(0)
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

queue1.print_list()