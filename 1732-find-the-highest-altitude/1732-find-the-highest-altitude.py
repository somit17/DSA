class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_sum = 0
        max_sum = 0
        for i in range(len(gain)):
            curr_sum+=gain[i]
            max_sum = max(curr_sum,max_sum)
        return max_sum
        #print(max_sum)