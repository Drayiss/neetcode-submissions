class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquaredSum(num):
            str_num = str(num)
            return sum(int(digit)**2 for digit in str_num)

        slow = fast = n

        while slow != 1:
            slow = getSquaredSum(slow)
            fast = getSquaredSum(fast)
            fast = getSquaredSum(fast)
            if slow == fast and slow != 1:
                return False

        return True