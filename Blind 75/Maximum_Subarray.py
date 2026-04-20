"""Problem 53 - Maximum Subarray
   Link - https://leetcode.com/problems/maximum-subarray/description/
   
   Question - Given an integer array nums, find the subarray with the largest sum, and return its sum."""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_sum = 0
        maximum_sum = nums[0]

        for num in nums:
            current_sum += num
            current_sum = max(current_sum,num)
            maximum_sum = max(current_sum,maximum_sum)
        return maximum_sum


