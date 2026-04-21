"""Problem 3 - Longest Substring Without Repeating Characters
   Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=oizxjoit
   
   Question - Given a string s, find the length of the longest substring without duplicate characters."""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        ret = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ret = max(ret, right - left + 1)

        return ret