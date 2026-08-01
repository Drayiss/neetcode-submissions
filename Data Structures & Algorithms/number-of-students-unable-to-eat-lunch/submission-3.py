from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = {0: 0, 1: 0}
        for pref in students:
            if pref not in count:
                count[pref] = 0
            count[pref] += 1

        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
                res -= 1
            else:
                return res
        
        return res