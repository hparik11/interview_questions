"""
731. My Calendar II
Medium

963

109

Add to List

Share
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked.
myCalendarTwo.book(50, 60); // return True, The event can be booked.
myCalendarTwo.book(10, 40); // return True, The event can be double booked.
myCalendarTwo.book(5, 15);  // return False, The event ca not be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
"""


class MyCalendarTwo(object):

    def __init__(self):
        self.positions = []
        self.count = {}

    def book(self, start, end):

        # Find position in sorted array
        i = bisect.bisect_left(self.positions, start)
        j = bisect.bisect_left(self.positions, end)

        print(self.positions, self.count, i, j)

        # if any START points have count >= 2 in range i<->j
        # it means that this is third overlap
        for k in range(i, j):
            if self.count[self.positions[k]] >= 2:
                return False

        # Register START point in count Map if not present
        if start not in self.count:
            # Initialize start count same as prev element
            # For current interval being added, count of all points
            # overlapping it will be incremented in last line, not here
            startCount = self.count[self.positions[i - 1]] if i - 1 >= 0 else 0

            # Handling edge case where start point before i is occupied/overlapped
            # with 2 intervals
            if startCount >= 2:
                return False

            self.positions.insert(i, start)

            # since we just now inserted in positions array
            # increment j for correct index
            j += 1

            # Register our new start point in count map
            self.count[start] = startCount

        # Register END point
        if end not in self.count:
            self.positions.insert(j, end)
            # Same as prev point
            self.count[end] = self.count[self.positions[j - 1]]

        # -- Crux of Logic --
        # Increment EVERY point in between i<->j
        # signifying that new interval overlapped these points
        for k in range(i, j):
            self.count[self.positions[k]] += 1

        return True
