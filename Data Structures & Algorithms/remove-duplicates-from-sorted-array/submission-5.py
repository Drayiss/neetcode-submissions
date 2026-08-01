
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_sorted = sorted(set(nums))
        nums[:len(unique_sorted)] = unique_sorted
        return len(unique_sorted)