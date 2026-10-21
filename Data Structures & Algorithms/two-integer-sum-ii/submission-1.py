class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            left_num = numbers[l]
            right_num = numbers[r]
            curr_sum = left_num + right_num

            if curr_sum == target:
                return [l + 1, r + 1]

            if curr_sum < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]