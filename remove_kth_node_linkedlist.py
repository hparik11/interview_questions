def removeKthNodeFromEnd(head, k):
    # Write your code here.
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next

    i = 0
    result = head
    print(count - k)
    print(result.value)
    if count - k - 1 > 0:
        while i < count - k - 1:
            result = result.next
            print(result.value)
            i += 1

    # result.value = result.next.value
    result.next = result.next.next
    return head


# Add, edit, or remove tests in this file.
# Treat it as your playground!


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

test1 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(removeKthNodeFromEnd(test1, 8).getNodesInArray())