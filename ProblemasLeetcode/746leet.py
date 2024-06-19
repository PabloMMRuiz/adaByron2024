from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        elif n == 2:
            return min(cost)

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

#el coste de subir a un piso es ese mas el minimo de los dos anteriores
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
#para llegar al último podemos llegar x el ultimo o el penultimo
        return min(dp[-1], dp[-2])