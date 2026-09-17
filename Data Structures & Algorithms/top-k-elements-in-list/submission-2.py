from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        n = len(nums)
        freq_index_to_num = [[] for _ in range(n + 1)]

        for num, count in num_to_count.items():
            freq_index_to_num[count].append(num)

        res = []
        for i in range(n, -1, -1):
            for num in freq_index_to_num[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
        