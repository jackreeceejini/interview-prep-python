# Queue bootcamp

import collections

class Queue:
    def __init__(self) -> None:
        self._data = collections.deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)

def binary_tree_depth_order(tree):
    """
    Traverse a binary tree in depth order return 
    nodes at each level from root to leaves
    """
    results = []
    if not tree:
        return results
    
    current_children = [tree]
    while current_children:
        results.append([curr.data for curr in current_children])
        current_children = [child for curr in current_children for child in (curr.left, curr.right) if child]
    return results 