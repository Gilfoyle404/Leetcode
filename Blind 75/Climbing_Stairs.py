"""Problem 70 - Climbing Stairs
   Link - https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=w1thoc57
   
   Question - You are climbing a staircase. It takes n steps to reach the top.
              Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return n
        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3,n):
            cur = prev1+prev2
            prev2 = prev1
            prev1 = cur
        return cur