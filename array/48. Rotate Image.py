class Solution(object):
    def rotate(self, matrix):
        """
        time: O(n*2)
        space: O(1)
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        #transpose
        for i in range(len(matrix)): 
            for j in range(i, len(matrix)): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        #swap columns
        i = 0 
        j = len(matrix) - 1
        while i < j: 
            for k in range(len(matrix)): 
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
            i += 1
            j -= 1
