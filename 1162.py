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

#Faster Solution
def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        res = 0
        while dq:
            r0, c0 = dq.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < n and 0 <= c1 < n and not grid[r1][c1]:
                    dq.append((r1, c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    res = max(res, grid[r1][c1])
        return res - 1
