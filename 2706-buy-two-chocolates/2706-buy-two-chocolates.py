class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        choc1 = prices[0]
        choc2 = prices[1]
        if choc1 + choc2 <= money:
            return money - (choc1 + choc2)
        return money