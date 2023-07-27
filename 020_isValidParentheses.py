class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

    def isValid(self, s: str) -> bool:
        stack = []
        mappings = { ")" :"(", "]" : "[", "}" : "{"}

        for c in s:
            if c in mappings:
                if stack:
                    if stack[-1] == mappings[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return not stack

"""
20. Valid Parentheses
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
2,568,271
Submissions
6,296,563
"""