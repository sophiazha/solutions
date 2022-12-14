class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]

    def numDistinct3(selfself, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i +1, j + 1) + dfs( i +1 , j)
            else:
                cache[(i,j)] = dfs(i +1 , j)
            return cache[(i,j)]
        return dfs(0,0)

    def numDistinct2(self, s: str, t: str) -> int:
        memo = {}
        def uniqueSubsequences(i, j):
            M, N = len(s), len(t)
            if i == M or j == N:
                return int(j == len(t))
            if (i, j) in memo:
                return memo[i, j]
            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)
            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)
            memo[i, j] = ans
            return ans
        return uniqueSubsequences(0, 0)
    """
    115. Distinct Subsequences
Hard

4438

178

Add to List

Share
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of 
the characters without disturbing the remaining characters' relative positions. 
(i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
Accepted
255,281
Submissions
586,300"""
