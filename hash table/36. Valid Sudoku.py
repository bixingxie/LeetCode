class Solution:
    def isValidSudoku(self, board):
        """
        time: O(n*2)
        space: O(1)
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #check row 
        for row in board: 
            visited = set()
            for val in row: 
                if val != '.':
                    if val in visited: return False
                    visited.add(val)
                    
        #check column 
        for rowNum in range(9): 
            visited = set()
            for colNum in range(9): 
                val = board[colNum][rowNum]
                if val != '.':
                    if val in visited: return False
                    visited.add(val)
                    
        #check neighbors 
        for rowNum in range(0, 7, 3): 
            for colNum in range(0, 7, 3): 
                visited = set()
                for i in range(rowNum, rowNum + 3): 
                    for j in range(colNum, colNum + 3): 
                        val = board[i][j]
                        if val != '.':
                            if val in visited: return False
                            visited.add(val)

        return True
