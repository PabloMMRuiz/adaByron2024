import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1)==0 or len(nums2)==0:
            return []
        min_heap = []

        for i in range(min(len(nums2),k)):
            heapq.heappush(min_heap, (nums1[0]+nums2[i],[0,i]))
        
        res = []
        while len(min_heap)!=0 and len(res)<k:
            sum, pair = heapq.heappop(min_heap)
            i = pair[0]
            j = pair[1]
            res.append([nums1[i],nums2[j]])
            if i+1<len(nums1):
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j],[i+1,j]))
        return res