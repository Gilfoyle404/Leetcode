"""Problem 217 - Contains Duplicate
   Link - https://leetcode.com/problems/contains-duplicate/description/
   
   Question - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = list(set(nums))
        return(len(set1)!=len(nums))

