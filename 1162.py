#Easy solution

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        lands, waters = [], []
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    lands.append([r,c])
                else:
                    waters.append([r,c])
        if (len(lands) == 0) or (len(waters)==0):
            return -1
            
        max_ = -1
        for water in waters:
            dists = []
            for land in lands:
                dist = abs(water[0] - land[0]) + abs(water[1] - land[1])
                dists.append(dist)
            max_ = max(max_, min(dists))

        return max_

