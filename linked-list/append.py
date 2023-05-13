"""
append, prepend, insert, pop, pop_first, pop_middle,
search, reverse, sort, merge
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #=====================================================================

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        return True

    #=====================================================================

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

        return True
    
    #=====================================================================

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True
        
        temp = self.head
        new_node.next = temp
        self.head = new_node
        
        return True
    
    #=====================================================================

    def insert(self, data, position):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True
        
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node

        return True
    
    #=====================================================================

    def pop(self):
        if self.head is None:
            return None
        
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        
        prev.next = None

        return temp
    
    #=====================================================================

    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head
        self.head = temp.next
        temp.next = None

        return temp

    #=====================================================================


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.print_list()

print()

linked_list2 = LinkedList()
linked_list2.prepend(10)
linked_list2.prepend(9)
linked_list2.prepend(8)
linked_list2.prepend(7)

linked_list2.print_list()

print()

linked_list3 = LinkedList()
linked_list3.append(0)
linked_list3.append(1)
linked_list3.append(2)
linked_list3.append(3)
linked_list3.insert(10, 2)
linked_list3.insert(10, 5)

linked_list3.print_list()

print()

linked_list4 = LinkedList()
linked_list4.append(0)
linked_list4.append(1)
linked_list4.append(2)
linked_list4.append(3)
linked_list4.pop()

linked_list4.print_list()

print()

linked_list5 = LinkedList()
linked_list5.append(0)
linked_list5.append(1)
linked_list5.append(2)
linked_list5.append(3)
linked_list5.pop_first()

linked_list5.print_list()