class Solution:
    def isHappy(self, n: int) -> bool:
        def get_squared_sum(num):
            str_num = str(num)
            return sum(int(digit)**2 for digit in str_num)

        slow = fast = n
        while slow != 1:
            slow = get_squared_sum(slow)
            fast = get_squared_sum(fast)
            fast = get_squared_sum(fast)
            if slow == fast and slow != 1:
                return False

        return True