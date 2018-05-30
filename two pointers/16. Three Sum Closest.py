class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort() 
        #[-4, -1, 1, 2]
        
        #using diff is essential for correctness** 
        #optimized, 89%
        res = 0 
        diff = float("inf")
        
        for index, value in enumerate(nums): 
            
            start, end = index + 1, len(nums)-1
            
            while start < end:
                curr = value + nums[start] + nums[end]
                if curr == target: 
                    return target
                
                if abs(curr - target) < diff:
                        res = curr
                        diff = abs(curr - target)
                elif curr < target: 
                    start += 1
                else: 
                    end -= 1
                    
        return res