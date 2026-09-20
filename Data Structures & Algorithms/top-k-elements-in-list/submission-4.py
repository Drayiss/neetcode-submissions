class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        n = len(nums)
        freq = [[] for _ in range(n + 1)]

        for num, count in num_to_count.items():
            freq[count].append(num)
        
        res = []
        for i in range(n, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
            

