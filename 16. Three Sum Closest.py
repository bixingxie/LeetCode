class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        
        nums.sort() 
        #[-4, -1, 1, 2]
        res = float("-inf")
        
        for index, value in enumerate(nums): 
            start, end = index + 1, len(nums)-1
            while start < end:
                curr = value + nums[start] + nums[end]
                if curr == target: 
                    return target

                if abs(res - target) > abs(curr - target): 
                        res = curr
                        
                elif curr < target: 
                    start += 1
                else: 
                    end -= 1
                    
        return res
                

