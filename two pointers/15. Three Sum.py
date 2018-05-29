class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<3):
            return []
        
        #optimized by avoiding calculating duplicates, 96%
        
        nums.sort()
        res = []
        
        for index, value in enumerate(nums):
            if index >= 1 and value == nums[index-1]:
                continue
            if value <= 0:
                start, end = index + 1, len(nums)-1
                target = -value
                
                while start < end: 
                    if nums[start] + nums[end] < target:
                        start += 1
                    elif nums[start] + nums[end] > target: 
                        end -= 1
                    else: #sum matches the target
                        res.append([value, nums[start], nums[end]])
                        while start < end and nums[start] == nums[start+1]:
                            start += 1
                        while start < end and nums[end] == nums[end-1]:
                            end -= 1
                        start += 1
                        end -= 1
                         
            else:
                pass 

        return res
