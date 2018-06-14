class Solution:
    def search(self, nums, target):
        """
        modified binary search
        time: O(log(n))
        space: O(1)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low, high = 0, len(nums)-1

        while low <= high: 
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[low] >= target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
