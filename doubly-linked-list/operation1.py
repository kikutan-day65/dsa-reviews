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

    def list_length(self):
        if self.head == None:
            return 0

        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

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

    def insert(self, data, position):
        if position == 0:
            return self.prepend(data)
        
        elif position == self.list_length():
            return self.append(data)
        
        new_node = Node(data)

        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

        return True
    
    #============================================

    def pop(self):
        if self.head == None:
            return None
        
        if self.head.next == None:
            temp = self.head
            self.head = None
            return temp
        
        temp = self.head
        before = self.head
        while temp.next:
            before = temp
            temp = temp.next

        before.next = None
        temp.prev = None

        return temp

    
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

linked_list3 = DoublyLinkedList()
linked_list3.append(0)
linked_list3.append(1)
linked_list3.append(2)
linked_list3.append(3)
linked_list3.insert(10, 2)
linked_list3.insert(20, 5)

linked_list3.print_list()

print()

linked_list4 = DoublyLinkedList()
linked_list4.append(0)
linked_list4.append(1)
linked_list4.append(2)
linked_list4.append(3)
linked_list4.pop()

linked_list4.print_list()

print()