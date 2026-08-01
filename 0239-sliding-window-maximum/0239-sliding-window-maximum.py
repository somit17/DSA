class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        for r in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)

            if queue[0] < r - k + 1:
                queue.popleft()

            if r >= k-1:
                result.append(nums[queue[0]])
        return result