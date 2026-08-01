import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # my_heap = []
        # for num in nums:
        #     heapq.heappush(my_heap, num)
        #     if len(my_heap) > k:
        #         heapq.heappop(my_heap)
        # return my_heap[0]
        return heapq.nlargest(k, nums)[-1]
        