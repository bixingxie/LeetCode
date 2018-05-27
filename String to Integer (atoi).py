class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        if(str == None or len(str) == 0):
            return 0
            
        d = {}
        sign = 1
        res = ''
        digitFlag = False
        
        for index, value in enumerate(str): 
            if value.isdigit():
                res += value 
                digitFlag = True
            else: 
                if digitFlag == False:
                    if(value == '-'):
                        sign = -1
                else:
                    break
        
        if(res == ''):
            return 0 
        else: 
            if(sign == 1):
                if(int(res) > 2**31-1):
                    return 2**31-1
                else:
                    return int(res)
            else:
                if(-1 * int(res) < -2**31):
                    return -2**31
                else:
                    return -1 * int(res)


a = Solution()
print(a.myAtoi("words and 987"))

                
            

        
