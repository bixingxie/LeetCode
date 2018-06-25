class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        time: O(n)
        space: O(n)
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = {}
        for index, val in enumerate(nums): 
            if val in d and index - d[val] <= k: 
                return True 
            else:
                d[val] = index
        return False
