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