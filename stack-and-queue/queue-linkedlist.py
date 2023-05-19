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
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return True
        
        temp = self.front
        new_node.next = temp
        self.front = new_node

        return True
    
    #=====================================

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        temp = self.front
        prev = self.front
        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None
        
        return temp


queue1 = Queue()
queue1.enqueue(0)
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

queue1.print_list()

print()

queue2 = Queue()
queue2.enqueue(0)
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)
queue2.dequeue()

queue2.print_list()