class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: int
        """
        
        
        res = curr = 0 
        for bit in nums: 
            if bit: 
                curr += 1
            else: 
                res = max(res, curr)
                curr = 0 
        res = max(res, curr)
        return res
