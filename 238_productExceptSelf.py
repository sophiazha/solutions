from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in reversed(range(len(nums))):
#       for i in range(len(nums) -1, -1, -1):
#       same reversed range, but difficult to follow
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def productExceptSelfL(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0]*len(nums), [0] *len(nums)
        prefix[0] = 1
        postfix[len(nums) -1 ] = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i -1] * prefix[i-1]
        for i in range(len(nums) -2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]

        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))

"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Accepted
1,322,411
Submissions
2,051,780
"""