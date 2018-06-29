class Solution:
    def jump(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: int
        """
        
        njump = 0 
        prev_max, curr_max = 0, 0 
        for i in range(0, len(nums)-1): 
            curr_max = max(curr_max, i + nums[i])
            if i == prev_max: 
                njump += 1
                prev_max = curr_max 
        return njump
    
