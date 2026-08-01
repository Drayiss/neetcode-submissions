class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max, counter = 0, 0
        for num in nums:
            if num == 1:
                counter += 1
            if num == 0:
                counter = 0
            if counter > max:
                max = counter

        return max