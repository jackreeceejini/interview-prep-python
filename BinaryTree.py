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
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k: # k-th node must be in right subtree of tree
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1: # k-th is iter itself
            return tree
        else: # k-th node must be in left subtree of iter
            tree = tree.left

    return None # if k is between 1 and the tree size, this is unreacheable

def find_successor(node):
    """
    find the successor of a node in an inorder traversal 
    of a tree
    """

    if node.right:
        # successor is the leftmost element in node's right subtree
        node = node.right
        while node.left:
            node = node.left
        return node

    # find the closest ancestor whose left subtree contains node
    while node.parent and node.parent.right is node:
        node = node.parent
    # A return value of None means node does not have a successor i.e node
    # is the rightmost node in the tree
    return node.parent 

def inorder_traversal_O1space(tree):
    """
    O(1) space inorder traversal of a tree without
    recursion
    """
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # We came down to tree from prev
            if tree.left: # keep going left
                next = tree.left
            else:
                result.append(tree.data)
                # done with left, so go right if right is not empty otherwise,
                # go up
                next = tree.right or tree.parent
        elif tree.left is prev:
            # we came up to tree from its left child
            result.append(tree.data)
            # done with left, so go right if right is not empty, otherwise go up
            next = tree.right or tree.parent
        else: # done with both children, so move up
            next = tree.parent

        prev, tree = tree, next
    return result 

def binary_tree_from_preorder_inorder(preorder, inorder):
    """
    Build a binary tree from preorder and inorder traversal data
    """
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preoder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end]
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, root_inorder_idx),
            # recursively builds the right subtree.
            binary_tree_from_preorder_inorder_helper(preorder_start + 1 + left_subtree_size, preorder_end, root_inorder_idx + 1, inorder_end)

        )
    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))


def reconstruct_preorder(preorder):
    """
    Reconstruct BinaryTree from preorder traversal data
    with blanks indicating null nodes.
    e.g.
    [H, B, F, NULL, NULL, E, A, NULL, NULL, NULL, C, NULL, D, NULL, G, I, NULL, NULL, NULL]
    """

    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None
        
        # Node that reconstruct_preoder_helper updates preorder_iter.
        #so the order of the following two calls are critical
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
    return reconstruct_preorder_helper(iter(preorder))


def create_list_of_leaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    # first do the left subtree, and then do the right subtree
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)

def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right
    # computes the nodes from the root to the leftmost leaf followed by all
    # the leaves in subtree.

    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (([subtree] if is_boundary or is_leaf(subtree) else []) + left_boundary_and_leaves(
            subtree.left, is_boundary) + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)
        )

    # computes the leaves in left_to_right order followed by the rightmost 
    # leaf to the root path in subtree.

    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (right_boundary_and_leaves(subtree.left, is_boundary 
        and not subtree.right) + right_boundary_and_leaves(subtree.right, is_boundary)
        +([subtree] if is_boundary or is_leaf(subtree) else []))

    return ([tree] + left_boundary_and_leaves(tree.left, is_boundary=True)
    + right_boundary_and_leaves(tree.right, is_boundary=True) if tree else[])


def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            #populate left child's next field
            start_node.left.next = start_node.right
            # populate right child's next field if iter is not the last node
            # of level
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next
    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left