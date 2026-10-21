from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)

        count_to_nums = [[] for _ in range(n + 1)] 
        for num, count in counts.items():
            count_to_nums[count].append(num)
        
        res = []
        for i in range(len(count_to_nums) - 1, -1, -1):
            sublist = count_to_nums[i]
            for num in sublist:
                res.append(num)
                if len(res) == k:
                    return res

        return res