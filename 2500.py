class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0 #Storing the final answer
        #Sort all the row
        for i in range(len(grid)):
            grid[i] = sorted(grid[i])
        #Find sum of max of each column
        for j in range(len(grid[0])):
            res += max([grid[i][j] for i in range(len(grid))])
        return res
