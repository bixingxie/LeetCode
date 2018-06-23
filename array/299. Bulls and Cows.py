class Solution(object):
    def getHint(self, secret, guess):
        """
        time: O(n)
        space: O(n)
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        bull = 0 
        cow = 0
        d = {}
        ind_lst = []
        for index, val in enumerate(secret): 
            if val == guess[index]: 
                bull += 1
            else:
                ind_lst.append(index)
                if val not in d: 
                    d[val] = 1
                else:
                    d[val] += 1
                    
        for i in ind_lst: 
            if guess[i] in d: 
                cow += 1
                if d[guess[i]] == 1: 
                    del d[guess[i]]
                else:
                    d[guess[i]] -= 1
        
        return "%dA%dB" % (bull, cow)
