class Solution:
    def containsDuplicate(self, nums):
        """
        time: O(n)
        space: O(n)
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
    
        # d = {}
        # for elem in nums: 
        #     if elem in d: 
        #         return True
        #     else:
        #         d[elem] = None
        # return False
