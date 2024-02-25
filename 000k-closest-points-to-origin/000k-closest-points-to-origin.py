import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for ind, point in enumerate(points):
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
            
        ans=[i[1] for i in heap]

        return ans
