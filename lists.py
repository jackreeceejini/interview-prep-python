
class ListNode:
    def __init__(self, data=0, next_node=None):
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


def overlapping_no_cycle_lists(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 # L2 is the longer list
    #Advances the longer list to get equal length lists.
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1 #None implies there is no overlap between L1 and L2

def delete_from_list(node_to_delete):
    # Assumes node_to_delete is not tail
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next

def remove_kth_last(L, k):
    """
    Assumes L has at least k nodes, deletes the k-th last node in L
    """

    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor
    second.next = second.next.next
    return dummy_head.next 


def remove_duplicates(L):
    it = L
    while it:
        # uses next_distinct to find the next distinct value
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L 

def cyclic_shift_right(L, k):
    if not L:
        return L
    
    # computes the length of L and the tail
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next
    
    k %= n
    if k == 0:
        return L
    
    tail.next = L # makes a cycle by connecting the tail to the head
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next
    
    new_head = new_tail.next

    new_tail.next = None
    return new_head 
    

def even_odd_merge(L):
    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next 
        turn ^= 1 # Alternate between even and odd
    tails[1].next = None
    tails[0].next = odd_dummy_head.next 
    return even_dummy_head

def is_linked_list_a_palindrome(L):
    # Finds the second half of L
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # Compares the first half and the reversed second half lists
    first_half_iter, second_half_iter = L, reversed_linked_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next, first_half_iter.next)
    return True


def list_pivoting(L, x):
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    #populates the 3 lists
    while L:
        if L.data < x:
            less_iter.next = L
            less_iter = less_iter.next 
        elif L.data == x:
            equal_iter.next = L 
            equal_iter = equal_iter.next
        else:
            # L.data > x:
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next

    # combining all lists
    greater_iter.next = None
    equal_iter.next = greater_head.next 
    less_iter.next = equal_head.next 
    return less_head.next  


def add_two_numbers(L1, L2):
    dummy_head = place_iter = ListNode()

    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next 
    return dummy_head.next 
