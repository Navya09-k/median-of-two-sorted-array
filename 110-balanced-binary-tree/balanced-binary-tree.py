class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(node):
            if not node: return 0
            l, r = h(node.left), h(node.right)
            if l == -1 or r == -1 or abs(l-r) > 1: return -1
            return max(l, r) + 1
        return h(root) != -1