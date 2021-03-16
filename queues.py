# Queue bootcamp

import collections

class Queue:
    """A basic queue implementation
    """
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


class Queue1:
    """
    A queue a more sophisticated queue whose 
    total size increase according to how full it is
    """
    SCALE_FACTOR = 2

    def __init__(self, capacity) -> None:
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries): # needs to resize
            # makes the queue elements appear consecutively
            self._entries(self._entries[self._head:] + self._entries[:self._head])
            # Resets head and tail
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1
    
    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret

    def size(self):
        return self._num_queue_elements 

    