"""
895. Maximum Frequency Stack

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
 

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""

import heapq


class Freq:
    def __init__(self, freq, index):
        self.freq = freq
        self.index = index

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.index > other.index
        return self.freq > other.freq


class FreqStack:

    def __init__(self):
        self.heap = []
        self.m = {}
        self.index = 0

    def push(self, x):
        if x in self.m:
            self.m[x] += 1
        else:
            self.m[x] = 1

        heapq.heappush(self.heap, (Freq(self.m[x], self.index), x))

        self.index += 1

    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        print(self.m, self.heap[0][0].freq)
        self.m[toBeRemoved[1]] -= 1
        return toBeRemoved[1]


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
