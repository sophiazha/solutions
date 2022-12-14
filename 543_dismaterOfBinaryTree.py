# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def longest_path(root):
            nonlocal res

            if not root:
                return 0
            left = longest_path(root.left)
            right = longest_path(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        longest_path(root)
        return res

    #below print detail recursive call stack
    def diameterOfBinaryTreeL(self, root: Optional[TreeNode]) -> int:
        level = ":"
        dia = 0

        def longest_path(node: TreeNode):
            nonlocal level
            level += "  "
            print(level, end='')
            if not node:
                print(None)
                level = level[0:-2]
                return 0
            else:
                print(node.val)
            nonlocal dia
            left = longest_path(node.left)
            right = longest_path(node.right)

            dia = max(dia, left + right)
            print(level + "for " + str(node.val) + " dia = " + str(dia) + " left= " + str(left) + " right= " + str(
                right) + " return: " + str(max(left, right) + 1))
            level = level[0:-2]
            return max(left, right) + 1

        longest_path(root)
        print("dia = " + str(dia))
        return dia
"""
543. Diameter of Binary Tree
Easy

9344

581

Add to List

Share
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
Accepted
859,271
Submissions
1,545,299
"""