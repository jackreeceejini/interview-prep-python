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


