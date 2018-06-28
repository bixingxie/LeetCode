class Solution(object):
    def canJump(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: bool
        """
        
        end = len(nums)-1
        for i in range(end, -1, -1): 
            if i + nums[i] >= end: 
                end = i 
        return end == 0
    
    
