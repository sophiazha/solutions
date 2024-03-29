from functools import lru_cache
from typing import List, Tuple


class Solution:
    def canPartition0(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False


    def canPartition(self, nums: List[int]) -> bool:  #brutal force, T(2^n) S(n)， not good
        #List is not hashable, so @lru_cache(maxsize=None) does not work here
        def dfs(nums: List[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(nums, n - 1, subset_sum)

    def canPartition2(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            print("call dfs n = " + str(n) + ", subset_sum = " + str(subset_sum))
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)

    def canPartitionA(self, nums: List[int]) -> bool:  # based on 2 dimesion array
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (half + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, len(nums) + 1):
            curr = nums[i - 1]
            for j in range(0, half + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][half]

    def canPartitionL(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total //2

        for n in nums:
            nextDp = set()
            for u in dp:
                if u + n == target:
                    return True
                else:
                    nextDp.add( u + n)
                    nextDp.add( u )
            dp = nextDp
        return False

nums = [1,5,11,5]
nums = [1,5,9,5]
sol = Solution()
#print(sol.canPartition0(nums))
#print(sol.canPartition(nums))
print(sol.canPartition(nums))



"""
416. Partition Equal Subset Sum
Medium

8922

150

Add to List

Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
Accepted
530,609
Submissions
1,136,219
"""