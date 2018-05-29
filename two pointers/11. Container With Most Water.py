class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        #two-pointer, O(n), 70%
        start = 0
        end = len(height)-1
        n = (end-start)*min(height[start], height[end])
        

        while start < end:
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
            n = max(n, (end-start)*min(height[start], height[end]))

        return n

        #bruteforce, O(n^2), time exceeded
        '''
        n = 0
        for i, val in enumerate(height):
            for j in range(i+1, len(height)):
                area = (j-i) * min(val, height[j])
                n = max(area, n)

        return n
        '''
        

        
        
