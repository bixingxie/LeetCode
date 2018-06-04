class Solution:
    def isNStraightHand(self, hand, W):
        """
        time: O(n*2)
        space: O(1)
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        hand.sort()
        while hand: 
            try: 
                num = hand[0]
                for i in range(W):
                    hand.remove(num + i)
            except:
                return False
        return True
            
            
            
        
