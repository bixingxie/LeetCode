class Solution(object):
    def firstMissingPositive(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums or len(nums) == 0: return 1
        i = 0 
        while i < len(nums): 
            if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]: 
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for ind in range(len(nums)): 
            if nums[ind] != ind + 1: 
                return ind + 1
        return len(nums)+1
            
