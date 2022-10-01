class Solution:
    def inorder(self,root):
        if root is None:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root)[k-1]