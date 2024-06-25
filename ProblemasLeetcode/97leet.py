class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        mem = {}
        
        def solve(p1: int, p2: int, p3: int) -> bool:
            if p3 == len(s3):
                return True
            
            if (p1, p2) in mem:
                return mem[(p1, p2)]
            
            ans = False
            if p1<len(s1) and s3[p3] == s1[p1]:
                ans = ans or solve(p1+1, p2, p3+1)

            if p2<len(s2) and s3[p3] == s2[p2]:
                ans = ans or solve(p1, p2+1, p3+1)
            
            mem[(p1, p2)] = ans
            
            return ans

        return solve(0, 0, 0)
