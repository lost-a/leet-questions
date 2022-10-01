class Solution:
    def inorder(self,root):
        if root is None:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return sorted(self.inorder(root1)+self.inorder(root2))