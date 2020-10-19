class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = None
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        # Write your code here.
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            heapq.heappush(self.minHeap, num)
        else:
            if num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -1 * num)
        
        self.rebalance()
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)
        self.updateMedian()
     
    def rebalance(self):
        
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                element = -1 * heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, element)
            else:
                element = -1 * heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, element)
            
            
    def updateMedian(self):
        
        if len(self.maxHeap) == len(self.minHeap):
            self.median = ((-1 * self.maxHeap[0]) + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            self.median = -1 * self.maxHeap[0]
        else:
            self.median = self.minHeap[0]

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()