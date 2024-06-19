class Solution:
    def tribonacci(self, n: int) -> int:
        info = {0:0,1:1,2:1}
        if n in info:
            return info[n]
        else:
            return self.aux(n,info)
        
    def aux(self,n,m):
        if n in m:
            return m[n]
        else:
            sum = self.aux(n-1,m)+self.aux(n-2,m)+self.aux(n-3,m)
            m[n] = sum
            return m[n]