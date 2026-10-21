class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums:
            # check if its the start of a sequence
            if num - 1 not in nums_set:
                next_num = num + 1
                length = 1
                while next_num in nums_set:
                    next_num += 1
                    length += 1
                longest_length = max(longest_length, length)
            
        return longest_length