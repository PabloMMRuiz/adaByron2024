import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pieras = [-s for s in stones]
        heapq.heapify(pieras)
        #heapq es minheap por defecto, asi que con un menos lo hacemos maxheap
        while len(pieras)>1:
            p1 = -heapq.heappop(pieras)
            p2 = -heapq.heappop(pieras)

            if p1 > p2:
                heapq.heappush(pieras, -(p1-p2))
        return -pieras[0] if len(pieras)==1 else 0


