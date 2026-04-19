"""Problem 2 - TWO SUM
   Link - https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=oizxjoit
   
   Question - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
              You may assume that each input would have exactly one solution, and you may not use the same element twice.
              You can return the answer in any order."""

#Using Hashmap

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i,v in enumerate(nums):
            if target-v in hashmap:
                return[i,hashmap[target-v]]
            else:
                hashmap[v] = i
            
