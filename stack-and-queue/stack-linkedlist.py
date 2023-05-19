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
    
    #================================
    
    def pop_first(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        temp = self.root
        self.root = self.root.next
        temp.next = None

        return temp



stack1 = Stack()
stack1.push(0)
stack1.push(1)
stack1.push(2)
stack1.push(3)

stack1.print_stack()

print()

stack2 = Stack()
stack2.push(0)
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.pop_first()

stack2.print_stack()