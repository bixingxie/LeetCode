import unittest

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #optimized, 93%
        ones = ['', 'I', "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ['', 'X', "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ['', 'C', "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ['', 'M', "MM", "MMM"]
            
        return thous[num//1000%10] + hunds[num//100%10] + tens[num//10%10] + ones[num%10]
    

#Test Driven Development
#Red --> Green -> Refactor

class UnitTest(unittest.TestCase):
    sol = Solution()

    def test(self):
        self.assertEqual(self.sol.intToRoman(1), "I")

if __name__ == '__main__':
    unittest.main()

