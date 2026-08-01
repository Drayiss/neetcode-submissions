import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = []
        for num in nums:
            heapq.heappush(my_heap, -num)
        for i in range(k):
            value = -heapq.heappop(my_heap)
        return value
        