class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m=nums[len(nums)//2]
        root=TreeNode(m)
        root.left=self.sortedArrayToBST(nums[:nums.index(m)])
        root.right=self.sortedArrayToBST(nums[nums.index(m)+1:])
        return root