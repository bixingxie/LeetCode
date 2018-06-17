class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        position = [10,8,0,5,3]
        targetLst = [2, 4, 12, 7, 9]
        speed =     [2, 4, 1, 1, 3]
        posLst =    [0, 0, 0, 0, 0]
        
        if not position or not speed: return False 
        for i in range(len(position)):
            
            
            

s = Solution()
print(s.carFleet(12, [10,8,0,5,3],[2,4,1,1,3]))
