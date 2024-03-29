from collections import deque
from typing import List

###################################L
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = set()

        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r, c):
            if r not in range(ROW) or c not in range(COL) \
                    or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island += 1
                    dfs(r, c)

        return island

    def numIslands1(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                    r not in range(rows)
                    or c not in range(cols)
                    or grid[r][c] == "0"
                    or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

    def numIslands3(self, grid: List[List[str]]) -> int:

        q = deque()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            q.append((r, c))

            while q:
                (r, c) = q.popleft()

                if r + 1 in range(rows) and (r + 1, c) not in visited \
                        and grid[r + 1][c] == "1":
                    q.append((r + 1, c))
                    visited.add((r + 1, c))
                if r - 1 in range(rows) and (r - 1, c) not in visited \
                        and grid[r - 1][c] == "1":
                    q.append((r - 1, c))
                    visited.add((r - 1, c))
                if c + 1 in range(cols) and (r, c + 1) not in visited \
                        and grid[r][c + 1] == "1":
                    q.append((r, c + 1))
                    visited.add((r, c + 1))
                if c - 1 in range(cols) and (r, c - 1) not in visited \
                        and grid[r][c - 1] == "1":
                    q.append((r, c - 1))
                    visited.add((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    visited.add((r, c))
                    island += 1

        return island

    def numIslandsL(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c ) not in visited :
                        q.append((r, c))
                        visited.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    island += 1
        return island

so = Solution()
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print(so.numIslandsL(grid))
# print(so.numIslands(grid))
# print(so.numIslands1(grid))
# print(so.numIslands2(grid))
# print(so.numIslands3(grid))

"""
200. Number of Islands
Medium

16940

389

Add to List

Share
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
Accepted
1,854,263
Submissions
3,318,927"""
