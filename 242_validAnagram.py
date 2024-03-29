from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    def isAnagramL(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            countS[ s[i] ] = countS[s[i]] + 1
            countT[ t[i] ] = countT[t[i]] + 1
        return countS == countT


xStr = "abcdefgabc"
yStr = "abcabcdefg"

solution = Solution()
print(solution.isAnagram( xStr, yStr))
"""
242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Accepted
1,605,719
Submissions
2,567,971"""

