'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        R = len(grid)
        C = len(grid[0])
        island = 0
        def dfs(r,c):
            if (r,c) not in visited and grid[r][c] == '1':
                visited.add((r,c))
                if r - 1 >= 0 : dfs(r-1 , c)
                if r < R - 1  : dfs(r+1 , c)
                if c - 1 >= 0 : dfs(r , c-1)
                if c < C - 1  : dfs(r , c+1)

        for row_index, row in enumerate(grid):
            for column_index, val in enumerate(row):
                if (row_index, column_index) not in visited  and grid[row_index][column_index] == '1':
                    island += 1
                    dfs(row_index, column_index)
                    # print(row_index, column_index, island, visited)
        return island
