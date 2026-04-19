"""Problem 268 - Missing Number
   Link - https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=oizxjoit
   
   Question - Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actual_sum = 0
        expeted_sum = 0
        for i in range(0,len(nums)+1):
            actual_sum += i
        for i in nums:
            expeted_sum += i

        return actual_sum-expeted_sum

        