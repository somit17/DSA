class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        curr_sum = 0
        for idx,cost in enumerate(costs):
            if curr_sum + cost <= coins:
                curr_sum+=cost
            else:
                return idx
        return len(costs)