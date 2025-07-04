class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None, 0
          
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)
          
            if left_depth > right_depth:
                return left_lca, left_depth + 1
            if left_depth < right_depth:
                return right_lca, right_depth + 1
          
            return node, left_depth + 1

        return dfs(root)[0]