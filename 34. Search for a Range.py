class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums)-1
        while low <= high: 
            mid = (low + high) // 2
            if nums[mid] == target:
                return self.findRange(nums, mid)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]
    
    def findRange(self, nums, mid):
        i = j = mid
        print(mid)
        while i > 0: 
            if nums[i-1] == nums[mid]:
                i -= 1
            else: 
                break 
        while j < len(nums)-1: 
            if nums[j+1] == nums[mid]:
                j += 1
            else:
                break 
        return [i, j]
