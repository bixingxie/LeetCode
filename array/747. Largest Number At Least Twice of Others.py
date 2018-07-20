class Solution(object):
    def dominantIndex(self, nums):
        """
        time = O(n)
        space = O(1)
        :type nums: List[int]
        :rtype: int
        """
        
        largest = max(nums)
        for num in nums: 
            if num != largest and num * 2 > largest: 
                return -1 
        return nums.index(largest)
            
