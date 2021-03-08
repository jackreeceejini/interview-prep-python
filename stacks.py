"""
Stack manipulations
"""
import math
import collections

Inf = math.inf

def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
    ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []
    
    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(self.ElementWithCachedMax(x, x if self.empty() else max(
            x, self.max())))


if __name__ == '__main__':
    items = [2,3,5,2,3,7,4,3,2]
    s = Stack()
    for item in items:
        s.push(item)
    print(s.max())
    
