"""
729. My Calendar I

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
"""
import bisect


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
