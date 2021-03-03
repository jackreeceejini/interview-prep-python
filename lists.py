
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