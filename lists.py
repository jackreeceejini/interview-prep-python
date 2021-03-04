
class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def search_list(L, key):
    while L and L.data != key:
        L = L.next
    
    # if key was not present in the list, L will have become null
    return L


def insert_after(node, new_node):
    """
    Insert new_node after node
    """
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    """
    Delete the node past this one. Assume node is not a tail
    """
    node.next = node.next.next

def merge_two_sorted_lists(L1, L2):
    # creates a placeholder for the result

    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    # append remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next 


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next 

    # Reverses sublist
    sublist_iter = sublist_head.next 
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
    return dummy_head.next



def has_cycle(head):
    """
    Checks if a linkedlist has a cycle
    """
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # finds the start of the cycle
            cycle_len_advanced_iter = head 
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            it = head 
            # Both iterators advance in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it # iter is the start of cycle
    return None # No cycle
