class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])   # sort by END
        arrows = 0
        shot_at = float('-inf')

        for s, e in points:
            if s > shot_at:               # starts after the last arrow's position
                arrows += 1               # need a new arrow
                shot_at = e               # shoot it at this balloon's end
        return arrows