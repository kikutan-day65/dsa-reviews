"""
- Evry parent node can have at most only 2 children
- must be a complete tree
- Every parent's key must be smaller than its chldren nodes

- representing our heap
    PARENT INDEX:   (index - 1) // 2
    LEFT CHILD INDEX:   2 * index + 1
    RIGHT CHILD INDEX:  2 * index + 2
"""

class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    #======================================================

    def get_parent_index(self, index):
        return (index - 1) // 2
    

    def get_left_child_index(self, index):
        return 2 * index + 1
    

    def  get_right_child_index(self, index):
        return 2 * index + 2
    
    #======================================================

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size
    
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size
    
    #======================================================

    def parent(self, index):
        return self.storage[self.get_parent_index(index)]
    

    def left_child(self, index):
        return self.storage[self.get_left_child_index(index)]
    

    def right_cihld(self, index):
        return self.storage[self.get_right_child_index(index)]
    
    #======================================================

    def is_full(self):
        return self.size == self.capacity
    

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    #======================================================
    
    def insert(self, data):
        if self.is_full():
            raise("Heap is full")
        
        self.storage[self.size] = data
        self.size += 1
        self.heapify_up()

    #======================================================
    
    def heapify_up(self):
        index = self.size - 1

        while self.has_parent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)
    
    #======================================================
