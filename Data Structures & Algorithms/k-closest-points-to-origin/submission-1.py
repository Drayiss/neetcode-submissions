class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(max_heap, (-dist, point[0], point[1]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            temp = heapq.heappop(max_heap)
            res.append([temp[1], temp[2]])

        return res