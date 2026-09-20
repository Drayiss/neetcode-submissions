from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_sublist = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                c_value = ord(c) - ord('a')
                count[c_value] += 1
            count_to_sublist[tuple(count)].append(s)
        
        res = []
        for sublist in count_to_sublist.values():
            res.append(sublist)
        
        return res