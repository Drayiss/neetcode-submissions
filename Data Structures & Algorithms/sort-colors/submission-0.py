class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        for num in nums:
            arr[num] += 1
        
        curr_index = 0
        for i in range(3):
            while arr[i] > 0:
                nums[curr_index] = i
                curr_index += 1
                arr[i] -= 1
        
        return nums