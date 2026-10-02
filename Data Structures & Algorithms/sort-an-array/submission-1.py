class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left = arr[l : m + 1]
            right = arr[m + 1 : r + 1]

            i = 0
            j = 0
            curr_index = l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[curr_index] = left[i]
                    i += 1
                else:
                    arr[curr_index] = right[j]
                    j += 1
                curr_index += 1
            
            while i < len(left):
                arr[curr_index] = left[i]
                i += 1
                curr_index += 1

            while j < len(right):
                arr[curr_index] = right[j]
                j += 1
                curr_index += 1

        
        def mergeSort(arr, l, r):
            if l >= r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)


        mergeSort(nums, 0, len(nums) - 1)
        return nums