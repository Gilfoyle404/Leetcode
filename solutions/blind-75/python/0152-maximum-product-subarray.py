"""Problem 152 - Maximum Product Subarray
   Link - http://leetcode.com/problems/maximum-product-subarray/description/
   
   Question - Given an integer array nums, find a subarray that has the largest product, and return the product.
              The test cases are generated so that the answer will fit in a 32-bit integer.
              Note that the product of an array with a single element is the value of that element."""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_minimum = 1
        current_maximum = 1
        max_product = max(nums)

        for num in nums:
            if num == 0:
                current_minimum = 1
                current_maximum = 1
                max_product = max(max_product, 0)
                continue

            prev_max = current_maximum
            prev_min = current_minimum

            current_maximum = max(num, prev_max * num, prev_min * num)
            current_minimum = min(num, prev_max * num, prev_min * num)

            max_product = max(max_product, current_maximum)

        return max_product