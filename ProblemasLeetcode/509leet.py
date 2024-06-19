class Solution:
    def fib(self, n: int) -> int:
        info = {0:0,1:1}
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.aux(n,{0:0,1:1})
        
    def aux(self,n,m):
        if n in m:
            return m[n]
        else:
            sum = self.aux(n-1,m)+self.aux(n-2,m)
            m[n] = sum
            return m[n]