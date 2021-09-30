#!/usr/bin/env python
# coding:utf-8
"""
@FileName : doordash_phone_screen.py
@Author   : Harsh Parikh
@Date     : 9/29/21 4:49 PM
"""


class Node:
    def __init__(self, key, value, status):
        self.key = key
        self.value = value
        self.status = status
        self.children = []

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value and self.status == other.status


def buildChildrenHashMap(menu: Node):
    menuHashmap = {}
    if not menu:
        return menuHashmap
    for child in menu.children:
        menuHashmap[child.key] = child

    return menuHashmap


def getModifiedCounts(oldMenu: Node, newMenu: Node):
    if not oldMenu and not newMenu:
        return 0

    count = 0
    if not oldMenu or not newMenu or oldMenu != newMenu:
        count += 1

    oldMenuChildren = buildChildrenHashMap(oldMenu)
    newMenuChildren = buildChildrenHashMap(newMenu)

    for child in oldMenuChildren.keys():
        count += getModifiedCounts(oldMenuChildren[child], newMenuChildren.get(child, None))

    for child in newMenuChildren.keys():
        if child not in oldMenuChildren:
            count += getModifiedCounts(None, newMenuChildren.get(child, None))

    return count


if __name__ == '__main__':
    a = Node("a", 1, True)
    b = Node("b", 2, True)
    c = Node("c", 3, True)
    d = Node("d", 4, True)
    e = Node("e", 5, True)
    f = Node("f", 6, True)
    g = Node("g", 7, True)

    a.children.append(b)
    a.children.append(c)

    b.children.append(d)
    b.children.append(e)

    c.children.append(f)

    a1 = Node("a", 1, True)
    # b1 = Node("b", 2, True)
    c1 = Node("c", 3, False)
    # d1 = Node("d", 4, True)
    # e1 = Node("e", 5, True)
    f1 = Node("f", 66, True)
    # g1 = Node("g", 7, False)

    # a1.children.append(b1)
    a1.children.append(c1)

    # b1.children.append(d1)
    # b1.children.append(e1)
    # b1.children.append(f1)

    c1.children.append(f1)

    print(getModifiedCounts(a, a1))
