class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
    
        l = 0
        r = n - 1
        m = (l + r) // 2

        left_half = nums[l : m + 1]
        right_half = nums[m + 1 : r + 1]

        def merge(arr1, arr2):
            i = 0
            j = 0
            res = []

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            
            while i < len(arr1):
                res.append(arr1[i])
                i += 1

            while j < len(arr2):
                res.append(arr2[j])
                j += 1
            
            return res


        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)
        return merge(left_half, right_half)

