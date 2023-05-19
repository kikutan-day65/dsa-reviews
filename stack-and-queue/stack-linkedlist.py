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
    
    #================================

    def print_stack(self):
        temp = self.root
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        return True
    
    #================================

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node

        return True


stack1 = Stack()
stack1.push(0)
stack1.push(1)
stack1.push(2)
print(stack1.is_empty())

stack1.print_stack()