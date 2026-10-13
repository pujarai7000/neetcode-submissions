class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        p=sorted(s)
        r=sorted(t)
        if p==r:
            return (True)
        else:
            return(False)