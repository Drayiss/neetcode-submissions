class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left_half = arr[l : m + 1]
            right_half = arr[m + 1 : r + 1]

            i = 0
            j = 0
            curr_index = l

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    arr[curr_index] = left_half[i]
                    i += 1
                else:
                    arr[curr_index] = right_half[j]
                    j += 1
                curr_index += 1
            
            while i < len(left_half):
                arr[curr_index] = left_half[i]
                i += 1
                curr_index += 1

            while j < len(right_half):
                arr[curr_index] = right_half[j]
                j += 1
                curr_index += 1

        def mergeSort(arr, l, r):
            if r - l + 1 <= 1:
                return

            m = (l + r) // 2
            
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

            


        mergeSort(nums, 0, len(nums) - 1)
        return nums