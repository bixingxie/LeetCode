class Solution:
    def removeDuplicates(self, nums):
        """
        time: O(n)
        space: O(n)
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0 
        i = 0
        d = {}
        for j in range(len(nums)):
            if nums[j] not in d: 
                d[nums[j]] = 1
            else:
                d[nums[j]] += 1
                
            if nums[j] != nums[i] or (nums[j] == nums[i] and d[nums[j]] == 2):
                i += 1
                nums[i] = nums[j] 
                
        return i+1
