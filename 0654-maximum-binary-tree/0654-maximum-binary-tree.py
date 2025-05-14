# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if len(nums) == 0: return None

            rootVal = max(nums)
            root = TreeNode(rootVal)
            
            left = nums[:nums.index(rootVal)]
            right = nums[nums.index(rootVal)+1:]

            root.left = dfs(left)
            root.right = dfs(right)

            return root

        return dfs(nums)