class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def isMagic(i, j): 
            if grid[i][j] != 5: return False 
            if grid[i-1][j-1] % 2 != 0 or grid[i-1][j+1] % 2 != 0 or grid[i+1][j-1] % 2 != 0 or grid[i+1][j+1] % 2 != 0: return False
            s = str(grid[i-1][j-1]) + str(grid[i-1][j]) + str(grid[i-1][j+1]) + str(grid[i][j+1]) + str(grid[i+1][j+1]) + str(grid[i+1][j]) + str(grid[i+1][j-1]) + str(grid[i][j-1])
            return s in "43816729" * 2 or s in "43816729"[::-1] * 2
                    
        return sum(isMagic(i, j) for i in range(1, len(grid)-1) for j in range(1, len(grid[i]) - 1))
                    
        
