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
    total size increases according to how full it is
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

    
class Queue2:
    """Building a queue using stacks
    """

    def __init__(self) -> None:
        self._enq, self._deq = [], []

    def enqueue(self, x):
        self._enq.append(x)

    def dequeue(self):
        if not self._deq:
            # Transfers the elements in _enq to _deq
            while self._enq:
                self._deq.append(self._enq.pop())
        if not self._deq: # _deq is still empty
            raise IndexError('empty queue')
        return self._deq.pop()


class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._candidates_for_max = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)
        # Eliminate dominated elements in _candidates_for_max
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if self._candidates_for_max[0] == result:
                self._candidates_for_max.popleft()
            return result
        raise IndexError('Empty Queue')

    def max(self):
        if self._candidates_for_max:
            return self._candidates_for_max[0]
        raise IndexError('empty queue')