class Solution:

    def twoSum(self, nums, target):
    	"""
        :type nums: List
        :type nums: Int
        :rtype: List
        """

        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]
            else:
                d[nums[i]] = i

        return []
