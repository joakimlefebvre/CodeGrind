from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt

            if not node or not node.val:
                return 0

            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return left_sum + right_sum + node.val

        valueSum(root)

        return total_tilt


def build_tree(root):
    if not root or root[0] is None:
        return None
    tree = TreeNode(root[0])
    parents = [tree]
    root.pop(0)
    kids = []
    while root:
        for p in parents:
            if root:
                p.left = TreeNode(root[0])
                kids.append(p.left)
                root.pop(0)
            if root:
                p.right = TreeNode(root[0])
                kids.append(p.right)
                root.pop(0)
        parents = kids
    return tree


if __name__ == "__main__":
    solution = Solution()
    root = [21, 7, 14, 1, 1, 2, 2, 3, 3]
    tree = build_tree(root)
    print(solution.findTilt(tree))
