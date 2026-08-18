class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            eating_rate = r - (r - l) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / eating_rate)
            
            if hours <= h:
                res = min(res, eating_rate)
                r = eating_rate - 1
            else:
                l = eating_rate + 1

        return res
