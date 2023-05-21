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
