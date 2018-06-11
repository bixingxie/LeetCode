class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        res = ''
        for i in range(len(shifts) - 1)[::-1]: 
            shifts[i] += shifts[i + 1]
        for index, shift in enumerate(shifts): 
            res += self.shift(S[index], shift)
        return res
                
    def shift(self, char, shift):
        return chr((ord(char) + shift - 97) % 26 + 97)
        
