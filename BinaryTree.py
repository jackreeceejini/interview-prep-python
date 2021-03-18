# BinaryTree activities
import collections


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left 
        self.right = right 


def is_symmetric(tree):
    """
    Check if Binary tree is symmetric
    """
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
            and check_symmetric(subtree_0.left, subtree_1.right)
            and check_symmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not
        return False
    return not tree or check_symmetric(tree.left, tree.right)


def lca(tree, node0, node1):
    """
    find lowest common ancestor of a tree 
    """
    Status = collections.namedtupble('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree
            return left_result
        right_result = lca_helper(tree.height, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree
            return right_result

        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes +
        int(tree is node0) + int(tree is node1))

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor 


def lcaWithParent(node_0, node_1):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth
    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
    # makes node_0 as the deeper node in order to simplify the code
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0

    # ascends from the deeper node
    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        node_0 = node_0.parent
        depth_diff -= 1

    # node ascends both nodes until we reach the LCA
    while node_0 is not node_1:
        node_0, node_1 = node_0.parent, node_1.parent 
    return node_0

def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right: #leaf
        return partial_path_sum
    return (sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum))

def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right: #leaf
        return remaining_weight == tree.data
    
    # non leaf
    return (has_path_sum(tree.left, remaining_weight - tree.data) or 
    has_path_sum(tree.right, remaining_weight - tree.data))

def inorder_traversal(tree):
    """
    Perform inorder traversal of a binary tree
    without recursion
    """
    s, result = [], []

    while s or tree:
        if tree:
            s.append(tree)
            # going left
            tree = tree.left
        else:
            # going up
            tree = s.pop()
            result.append(tree.data)
            # going right
            tree = tree.right
    return result

def preorder_traversal(tree):
    """
    return preorder_traversal without recursion
    """
    path, result = [tree], []

    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            curr += [curr.right, curr.left]
    return result

def find_kth_node_binary_tree(tree, k):
    while Tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k: # k-th node must be in right subtree of tree
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1: # k-th is iter itself
            return tree
        else: # k-th node must be in left subtree of iter
            tree = tree.left

    return None # if k is between 1 and the tree size, this is unreacheable

    

