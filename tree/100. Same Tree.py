class Solution:
    def isSameTree(self, p, q):
        """
        time: O(n)
        space: O(n)
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    
        if not p and not q: return True 
        elif not p or not q: return False 
        else: 
            if p.val != q.val: return False 
            else: return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
