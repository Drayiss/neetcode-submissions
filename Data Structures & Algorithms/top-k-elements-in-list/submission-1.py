from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        def freq(num):
            return count[num]

        unique_nums = list(count.keys())
        unique_nums.sort(key=freq, reverse=True)

        return unique_nums[0:k]