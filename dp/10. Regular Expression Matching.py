class Solution:
    def isMatch(self, s, p):
        #optimized, 90%, dp
        """
        :type s: str
        :type p: str
        :rtype: bool
        

            S 0 1 2 3
            0 1 2 3 4
              a b c d
    P 0     T F F F F
    0 1 a   F F F F F
    1 2 *   F F F F F
    2 3 .   F F F F F 
    3 4 c   F F F F F
    4 5 d   F F F F F

ab       abc*
abc      abc*
abccccc  abc*

        """

        x = len(s) + 1 #5
        y = len(p) + 1 #6
        if y == 1:
            return x == 1
        
        #Initilize a matrix of x * y
        matrix = [[False] * x for i in range(y)]
        #an empty s must match an empty p 
        matrix[0][0] = True
        
        for i in range(y-1):
            if p[i] == '*': 
                matrix[i+1][0] = matrix[i-1][0]

        for i in range(1, y):
            for j in range(1, x):
                if p[i-1] == '.':
                    matrix[i][j] = matrix[i-1][j-1] and True
                elif p[i-1] == '*':
                    if p[i-2] != s[j-1] and p[i-2] != '.':
                        matrix[i][j] = matrix[i-2][j]
                    else:
                        matrix[i][j] = matrix[i-2][j] or matrix[i-1][j] or matrix[i][j-1]
                else:
                    matrix[i][j] = matrix[i-1][j-1] and p[i-1] == s[j-1]
            

        return matrix[-1][-1]

s = Solution()
print(s.isMatch("aaa", "a*a"))
