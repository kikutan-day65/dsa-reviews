class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #============================================

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        return True
    
    #============================================

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return True
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

        return True
    
    #============================================

    def prepend(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return True
        
        temp = self.head
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node

        return True
    
    #============================================

    
linked_list = DoublyLinkedList()
linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.print_list()

print()

linked_list2 = DoublyLinkedList()
linked_list2.append(0)
linked_list2.append(1)
linked_list2.append(2)
linked_list2.append(3)
linked_list2.prepend(-1)
linked_list2.prepend(-2)

linked_list2.print_list()

print()