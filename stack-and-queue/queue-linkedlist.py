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
            print(temp.data)
            temp = temp.next
    
    #=====================================

    def is_empty(self, data):
        if self.front == None:
            return True
        return False