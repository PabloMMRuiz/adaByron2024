class Solution:
    def numTrees(self, n: int) -> int:
        d = [0 for i in range(n+1)]
        d[0] = d[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                d[i] += d[j-1] * d[i-j]
        return d[n]