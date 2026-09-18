from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prefix_sum_to_count[diff]
            prefix_sum_to_count[curr_sum] += 1
        
        return res