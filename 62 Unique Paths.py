'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:
1 <= m, n <= 100
'''
class Solution:
    mem = {}

    def func(self, m, n, r, c):
        if Solution.mem[r][c] != -1:
            return Solution.mem[r][c]
        
        ans = 0
        if r == m-1 and c == n-1:
            return 1
        if r + 1 < m and c < n:
            ans += self.func(m, n, r + 1, c)
        if r < m and c + 1 < n:
            ans += self.func(m, n, r, c + 1)
        
        Solution.mem[r][c] = ans
        return Solution.mem[r][c]


    def uniquePaths(self, m: int, n: int) -> int:
        Solution.mem = [[-1 for _ in range(n)] for _ in range(m)]
        return self.func(m, n, 0, 0)
