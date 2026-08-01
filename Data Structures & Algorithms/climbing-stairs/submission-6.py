class Solution:
    def climbStairs(self, n: int) -> int:
        # perfect solution
        one, two = 1, 2

        for _ in range(1, n):
            next = one + two
            one = two
            two = next
    
        return one