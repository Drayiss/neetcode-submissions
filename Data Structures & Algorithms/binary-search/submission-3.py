class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursiveSearch(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return recursiveSearch(l, mid - 1)
            else:
                return recursiveSearch(mid + 1, r)
        
        return recursiveSearch(0, len(nums) - 1)

        