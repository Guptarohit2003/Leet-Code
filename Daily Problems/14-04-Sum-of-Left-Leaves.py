# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0

            if not node.left and not node.right and is_left:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


print(
    Solution().sumOfLeftLeaves(
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    )
)  # 24
