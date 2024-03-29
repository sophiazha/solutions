from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return dp[(i, total)]

        return dfs(0, 0)

    def findTargetSumWaysL(self, nums: List[int], target: int) -> int:
        dp = {}  # index, currentTotal
        def backTrack(i, currentTotal):
            if i == len(nums) - 1:
                if currentTotal == target:
                    return 1
                else:
                    return 0
            if (i, currentTotal) in dp:
                return dp[(i, currentTotal)]

            dp[(i, currentTotal)] = backTrack(i + 1, currentTotal + nums[i + 1]) + backTrack(i + 1,
                                                                                             currentTotal - nums[i + 1])
            return dp[(i, currentTotal)]

        return backTrack(-1, 0)

"""
494. Target Sum
Medium

8099

293

Add to List

Share
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
 and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them 
to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
Accepted
405,703
Submissions
891,416"""










