"""
search, reverse
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

    def search_data(self, target):
        """
        data is in linked list -> True
        data isn't in linked list -> False
        """

        if self.head is None:
            return False
        
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
        return False
    
    #=====================================================================

    def search_at_index(self, potision):
        if self.head is None:
            return None
        
        temp = self.head
        for i in range(potision):
            temp = temp.next
        
        return temp.data
    
    #=====================================================================
    
    def reverse(self):
        """
        steps:
            1. store current.next in temp
            2. current.next points to prev
            3. prev is current
            4. current is temp
        """
        if self.head is None:
            return None
        
        prev = None
        current = self.head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        self.head = prev

        return self.head


# search_data
linked_list1 = LinkedList()
linked_list1.append(0)
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)

print(linked_list1.search_data(0))
print(linked_list1.search_data(3))
print(linked_list1.search_data(5))

print()

# search_at_index
linked_list2 = LinkedList()
linked_list2.append(0)
linked_list2.append(1)
linked_list2.append(2)
linked_list2.append(3)

print(linked_list2.search_at_index(0))
print(linked_list2.search_at_index(2))

print()

# reverse
linked_list3 = LinkedList()
linked_list3.append(0)
linked_list3.append(1)
linked_list3.append(2)
linked_list3.append(3)
linked_list3.reverse()

linked_list3.print_list()

print()