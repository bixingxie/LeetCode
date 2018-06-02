class Solution:
    def fourSum(self, nums, target):
        """
        time: O(n*3)
        space: O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        if len(nums) < 4: return res
        nums.sort()
        for index, a in enumerate(nums): 
            if index > 0 and a == nums[index - 1]: continue
            for  i in range (index+1, len(nums)):
                b = nums[i]
                if i > index + 1 and b == nums[i - 1]:
                    continue
                start = i + 1
                end = len(nums) - 1
                while start < end: 
                    c = nums[start]
                    d = nums[end]
                    if a + b + c + d == target:
                        res.append([a, b, c, d])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1  
                        start += 1
                        end -= 1
                    elif a + b + c + d > target: end -= 1
                    else: start += 1 
        return res