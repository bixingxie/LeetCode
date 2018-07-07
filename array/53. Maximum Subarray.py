class Solution(object):
    def maxSubArray(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: int
        """
        
        global_max = local_max = float("-inf")
        
        for num in nums: 
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)
        
        return global_max
