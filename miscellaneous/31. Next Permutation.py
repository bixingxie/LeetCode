class Solution:
    def nextPermutation(self, nums):
        """
        time: O(n)
        space: O(1)?
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 0: return []
        i = len(nums)-1
        while i > 0: 
            if nums[i] <= nums[i-1]: 
                i -= 1
            else:
                j = i
                pos = len(nums)-1
                while j < len(nums): 
                    if nums[j] <= nums[i-1]:
                        pos = j-1
                        break
                    else:
                        j += 1
                nums[pos], nums[i-1] = nums[i-1], nums[pos]
                nums[i:] = nums[i:][::-1]
                return
        nums.reverse()

