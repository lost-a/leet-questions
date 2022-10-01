class Solution:
    def solve(self,root,min_val,max_val):
        if root is None:
            return True
        if min_val<root.val<max_val:
            return self.solve(root.left,min_val,root.val) and self.solve(root.right,root.val,max_val)
        return False
        return self.solve(root.left)+[root.val]+self.solve(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        
        return self.solve(root, float('-inf'), float('inf'))