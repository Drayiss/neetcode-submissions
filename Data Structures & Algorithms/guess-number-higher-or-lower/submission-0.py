# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            mid = r - (r - l) // 2
            guess_num = guess(mid)
            if guess_num == -1: # guess > target
                r = mid - 1
            elif guess_num == 1: # guess < target
                l = mid + 1
            else:
                return mid
        return -1
            
            