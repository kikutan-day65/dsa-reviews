class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None
    
    #================================

    def is_empty(self):
        if self.root is None:
            return True
        return False
    


stack1 = Stack()
print(stack1.is_empty())