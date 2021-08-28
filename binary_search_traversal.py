from collections import deque


class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)


def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)


def post_order_print(root):
    if not root:
        return
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    print(root.data)


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]

            4
          /   \
         2     5
       /   \
      1     3
    """
    values = []
    stack = [root]

    while stack:
        top_node = stack.pop()
        if top_node:
            values.append(top_node.data)
            stack.append(top_node.r_child)
            stack.append(top_node.l_child)

    return values


# Iterative function for inorder tree traversal
def inOrder(root):
    """

    Args:
        root:

    Returns:

            4
          /   \
         2     5
       /   \
      1     3
    """
    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.l_child

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")  # Python 3 printing

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.r_child

        else:
            break


# Iterative function to perform post-order traversal of the tree
def postorderIterative(root):

    """

    Args:
        root:

    Returns:

            4
          /   \
         2     5
       /   \
      1     3
    """
    # create an empty stack and push root node
    stack = deque()
    stack.append(root)

    # create another stack to store post-order traversal
    out = deque()

    # loop till stack is empty
    while stack:

        # we pop a node from the stack and push the data to output stack
        curr = stack.pop()
        out.append(curr.data)

        # push left and right child of popped node to the stack
        if curr.l_child:
            stack.append(curr.l_child)

        if curr.r_child:
            stack.append(curr.r_child)

    # print post-order traversal
    while out:
        print(out.pop(), end=' ')


if __name__ == '__main__':
    """
            4
          /   \
         2     5
       /   \
      1     3
    """

    r = Node(4)
    binary_insert(r, Node(2))
    binary_insert(r, Node(1))
    binary_insert(r, Node(3))
    binary_insert(r, Node(5))

    # print("in order:")
    # in_order_print(r)
    #
    # print("pre order")
    # pre_order_print(r)
    #
    # print("post order")
    # post_order_print(r)

    print("pre order")
    print(preorderTraversal(root=r))
    print("in order:")
    print(inOrder(r))
    print("post order")
    print(postorderIterative(r))
