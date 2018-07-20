class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        time: O(n)
        space: O(1)
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        for i in range(len(nums)): 
            index = abs(nums[i]) - 1 
            if nums[index] > 0: 
                nums[index] = -nums[index]
        for i in range(len(nums)): 
            if nums[i] > 0: 
                res.append(i + 1)
        return res
        
