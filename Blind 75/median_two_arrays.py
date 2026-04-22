"""Problem 4 - Invert Binary Tree
   Link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
   
   Question - Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
              The overall run time complexity should be O(log (m+n))."""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = nums1+nums2
        merged_list.sort()
        if len(merged_list)%2 == 0:
            mid = len(merged_list)//2
            return (float(merged_list[mid]+merged_list[mid-1])/2)
        else:
            mid = len(merged_list)//2
            return merged_list[mid]      