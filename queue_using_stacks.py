class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            val = self.stack2[-1]
            del self.stack2[-1]
            return val
        elif self.stack1:
            for index in range(len(self.stack1)-1, -1, -1):
                self.stack2.append(self.stack1[index])
                del self.stack1[index]
            val = self.stack2[-1]
            del self.stack2[-1]
            return val
        else:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            for index in range(len(self.stack1)-1, -1, -1):
                self.stack2.append(self.stack1[index])
                del self.stack1[index]
            return self.stack2[-1]
        else:
            return None
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack2) == 0 and len(self.stack1) == 0



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
# param_5 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_4, param_3)