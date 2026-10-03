class Solution:
    def maxDifference(self, s: str) -> int:
        s_map = Counter(s)
        maxOdd = float('-inf')
        evenMin = float('inf')
        
        for k,v in s_map.items():
            if v & 1:
                maxOdd = max(maxOdd,v)
            else:
                evenMin = min(evenMin,v)

        return maxOdd - evenMin
