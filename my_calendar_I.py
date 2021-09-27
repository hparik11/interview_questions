class Node(object):
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.s >= end:
            if self.left is None:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.e <= start:
            if self.right is None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)


# O(N^2)
class MyCalendar1:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        if self.calendar:
            index = bisect.bisect_left(self.calendar, (start, end))

            if index != 0 and start < self.calendar[index - 1][1]:
                return False

            if index != len(self.calendar) and end > self.calendar[index][0]:
                return False

        bisect.insort_left(self.calendar, (start, end))

        return True
