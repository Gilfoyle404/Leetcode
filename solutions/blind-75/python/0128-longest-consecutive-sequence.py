"""Problem 1 - Longest_Concequtive_sequence
   Link - https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=oizxjoit
   
   Question - Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
              You must write an algorithm that runs in O(n) time."""

class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0
        for x in nums:
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y = y+1
                longest = max(longest,y-x)
        return longest