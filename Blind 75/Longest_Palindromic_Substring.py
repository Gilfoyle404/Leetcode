"""Problem 5 - Longest Palindromic Substring
   Link - https://leetcode.com/problems/longest-palindromic-substring/description/
   
   Question - Given a string s, return the longest palindromic substring in s."""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        best = ""

        for left in range(n):
            for right in range(left + 1, n + 1):
                sub = s[left:right]
                if sub == sub[::-1] and len(sub) > len(best):
                    best = sub

        return best