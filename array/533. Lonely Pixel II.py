class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        time: O(n**3)
        space: O(n)
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        res = 0 
        
        if not picture or len(picture) == 0: return 0 
        R, C =  len(picture), len(picture[0])
        row_black_nums = [row.count('B') for row in picture]
        col_black_nums = [0] * C
                    
        for c in range(C):
            for r in range(R): 
                if picture[r][c] == 'B': 
                    col_black_nums[c] += 1
        
        for r in range(R): 
            for c in range(C): 
                if picture[r][c] != 'B': 
                    continue 
                if not N == row_black_nums[r] == col_black_nums[c]:
                    continue 
                if picture.count(picture[r]) != N: 
                    continue
                res += 1
                        
        return res 
