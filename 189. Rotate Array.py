class Solution:
    def rotate(self, nums, k):
        """
        time: O(n)
        space: O(n)
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        if not k or len(nums) < 2: return
        nums[:] = nums[-k:] + nums[:-k]
