from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        # heap = []
        # for key,v in counter.items():
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
            #print(heap)
            # if len(heap) > k:
            #     heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        