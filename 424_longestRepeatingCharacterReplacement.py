class Solution:
    #my method can be better
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxf = 0, 0, 0
        freq = {}
        longest = 0
        for c in s:
            freq[c] = freq.get(c, 0) + 1
            maxf = max(maxf, freq[c])
            if (r - l + 1 - maxf) > k:
                freq[s[l]] = freq[s[l]] -1
                l += 1
            else:
                longest = max(longest, r - l + 1)
            r += 1
        return longest

    def characterReplacement2(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

    def characterReplacementL(self, s: str, k: int) -> int:  # can be further improved by below characterReplacementL2
        l, res, maxF, count = 0, 0, 0, {}

        for i, c in enumerate(s):  # enumerate better as it has both index and value
            count[c] = count.get(c, 0) + 1
            if i - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

    def characterReplacementL2(self, s: str, k: int) -> int:
        l, res, maxF, count = 0, 0, 0, {}

        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            maxF = max(maxF, count[c])
            if i - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

so = Solution()
s = "AABABBA"
k = 1
print(so.characterReplacement2(s, k))

"""
424. Longest Repeating Character Replacement
Medium

5849

229

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
Accepted
306,468
Submissions
597,995
"""
