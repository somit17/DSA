import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        #print(heap)
        heapq.heapify(heap)
        #print(heap)
        while len(heap) > 1:
            y = - heapq.heappop(heap)
            x = - heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,-(y - x))
        return -heap[0] if heap else 0