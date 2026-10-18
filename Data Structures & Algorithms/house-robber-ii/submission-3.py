class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        memos = [
            { 0: nums[0], 1: max(nums[0], nums[1]) },
            { 1: nums[1], 2: max(nums[1], nums[2]) }
        ]

        def opt(l, i):
            if i in memos[l]:
                return memos[l][i]

            memos[l][i] = max(
                opt(l, i - 1),
                nums[i] + opt(l, i - 2)
            )

            return memos[l][i]

        return max(
            opt(0, n - 2),
            opt(1, n - 1)
        )

