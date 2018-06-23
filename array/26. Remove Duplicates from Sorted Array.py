class Solution:
    def removeDuplicates(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: int
        """
        
        #two pointers: slow and fast 
        if len(nums) == 0: return 0
        i = 0 
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j] 
        return i+1
