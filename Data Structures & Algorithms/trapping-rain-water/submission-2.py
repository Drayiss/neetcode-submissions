class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        max_left = max_right = 0

        res = 0

        while l <= r:
            if max_left <= max_right:
                potential_water = max_left - height[l]
                res += max(potential_water, 0)
                max_left = max(max_left, height[l])
                l += 1
            else:
                potential_water = max_right - height[r]
                res += max(potential_water, 0)
                max_right = max(max_right, height[r])
                r -= 1

        return res