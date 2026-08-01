class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums:
            # check if its the start of a sequence
            if num - 1 not in nums_set:
                current_sequence_length = 1

                while num + current_sequence_length in nums_set:
                    current_sequence_length += 1
                    
                longest_length = max(longest_length, current_sequence_length)

        return longest_length