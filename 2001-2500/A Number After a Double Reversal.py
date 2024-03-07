class Solution:
    def isSameAfterReversals(self, reverse: int) -> bool:
        if reverse%10==0 and reverse!=0:
            return False
        return True

        
