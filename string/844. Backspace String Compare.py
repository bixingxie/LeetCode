class Solution:
    def backspaceCompare(self, S, T):
        """
        time = O(n*2), n = max(s, t)
        space = O(1)
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        i = 0
        while i < len(S):
            if i > 0 and S[i] == '#':
                S = S[:i-1] + S[i+1:]
                i -= 1
            elif S[i] == '#':
                S = S[1:]
            else:
                i += 1
            
        i = 0
        while i < len(T):
            if i > 0 and T[i] == '#':
                T = T[:i-1] + T[i+1:]
                i -= 1
            elif T[i] == '#':
                T = T[1:]
            else:
                i += 1
        
        return S == T
