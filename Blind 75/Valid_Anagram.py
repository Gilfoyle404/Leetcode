"""Problem 242 - Valid Anagram
   Link - https://leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=oizxjoit
   
   Question - Given two strings s and t, return true if t is an anagram of s, and false otherwise."""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = defaultdict(int)
        for i in s:
            count[i]+=1
        for i in t:
            count[i]-=1
        for value in count.values():
            if value!=0:
                return False
        return True

