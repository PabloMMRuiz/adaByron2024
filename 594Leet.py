from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dicc = Counter(nums)
        acc = 0
        for n in dicc.keys():
            if n + 1 in dicc:
                acc = max(acc, dicc[n] + dicc[n + 1])
        return acc