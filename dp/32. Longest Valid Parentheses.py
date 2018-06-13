class Solution:
    def longestValidParentheses(self, s):
        """
        time: O(n)
        space: O(n)
        :type s: str
        :rtype: int
        """
        #()(())
        #(())
        #0, 1, 2, 3
        if s == '': return 0 
        dp = [0] * len(s)
        
        for index, val in enumerate(s): 
            if val == ')' and index > 0:
                if s[index-1] == '(':
                    if index > 1:
                        dp[index] = dp[index-2] + 2
                    else:
                        dp[index] += 2
                else:
                    if index - dp[index-1] > 0 and s[index - dp[index-1] - 1] == '(':
                        if index - dp[index-1] > 1: 
                            dp[index] = dp[index-1] + dp[index - dp[index-1] - 2] + 2
                        else:
                            dp[index] = dp[index-1] + 2          
        return max(dp)
                
