import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
######################## L
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t, n = 0, len(grid)
        minH = [[grid[0][0], 0, 0]]
        visit = set()

        while minH:
            h, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (n - 1, n - 1):
                return h

            for (x, y) in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (x in range(n) and
                        y in range(n) and
                        (x, y) not in visit
                ):
                    heapq.heappush(minH, [max(h, grid[x][y]), x, y])


"""
778. Swim in Rising Water
Hard

2508

167

Add to List

Share
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if 
and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, 
you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.
Accepted
100,247
Submissions
168,555
"""