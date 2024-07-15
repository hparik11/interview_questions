#!/usr/bin/env python
# coding:utf-8
"""
@FileName : amazon_decision_tree.py
@Author   : Harsh Parikh
@Date     : 8/5/21 1:27 PM

Decision Tree Design Implement three methods
//   signal_value                  constant
//                        X1 < 3
//                       ------------
//           |                                 |
//       X2 < 1                        X1 < 6
//    -----------                        ---------
//  |              |                 |                  |
//  N             Y                N             X3 < 2
//                                                  ----------
//                                                  |          |
//                                                 Y          N

Test cases:
// {X1 <- 2, X2 <- 1, X3 <- 11} -> Y
// {X1 <- 8, X2 <- 4, X3 <- 12} -> N

write the class and implement the class with three method below.
use add Split to build the tree.

// class DecisionTree:

//   method add_split(leaf, signal_name, constant):
//     Add a split condition to the given leaf.
//     Return the newly created leaves for future calls.
//     Feel free to pass a sentinel value (like null) as the leaf for the first call to this method.
//     Subsequent calls should pass leaves returned by previous calls.

//   method set_leaf_value(leaf, value):
//     Set the return value for a leaf.

//   method evaluate(signals):
//     Evaluate the tree on a mapping of signal_name -> signal_value.
//     Return the value of the leaf reached by traversing the tree.
Most important point is to handle corner cases


"""


class Node(object):
    def __init__(self, signal=None, constant=None, is_leaf=False, left=None, right=None):
        self.signal = signal
        self.left = left
        self.right = right
        self.is_leaf = is_leaf
        self.constant = constant


class DecisionTree:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def add_split(leaf, signal_name, constant):
        # Add a split condition to the given leaf node.
        # Return the newly created leaves for future calls.
        # Subsequent calls should pass leaves returned by previous calls.
        leaf.signal = signal_name
        leaf.constant = constant
        leaf.left = Node()
        leaf.right = Node()
        return leaf.left, leaf.right

    @staticmethod
    def set_leaf_value(leaf, value):
        # Set the return value for a leaf node.
        leaf.is_leaf = True
        leaf.constant = value

    def evaluate(self, signals):
        # Evaluate the tree on a mapping of signal_name -> signal_value.
        # Return the value of the leaf node reached by traversing the tree.
        curr = self.root
        while not curr.is_leaf:
            if signals[curr.signal] < curr.constant:
                curr = curr.left
            else:
                curr = curr.right
        return curr.constant


if __name__ == '__main__':
    dt = DecisionTree()
    l, r = dt.add_split(dt.root, 'X1', 3)
    l1, r1 = dt.add_split(l, 'X2', 1)
    dt.set_leaf_value(l1, 'N')
    dt.set_leaf_value(r1, 'Y')

    l1, r1 = dt.add_split(r, 'X1', 6)
    dt.set_leaf_value(l1, 'N')
    l1, r1 = dt.add_split(r1, 'X3', 2)
    dt.set_leaf_value(l1, 'Y')
    dt.set_leaf_value(r1, 'N')

    # {'X1': 2, 'X2': 1, 'X3': 11} Y
    # {'X1': 8, 'X2': 4, 'X3': 12} N
    print(dt.evaluate({'X1': 2, 'X2': 1, 'X3': 11}))
    print(dt.evaluate({'X1': 8, 'X2': 4, 'X3': 12}))
