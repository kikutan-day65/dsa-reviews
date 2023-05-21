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
        self.capacity + capacity
        self.size = 0