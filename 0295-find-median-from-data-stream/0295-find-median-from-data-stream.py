import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap,-num)
        else:
            heapq.heappush(self.minheap,num)


        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (-self.maxheap[0]+self.minheap[0]) / 2 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()