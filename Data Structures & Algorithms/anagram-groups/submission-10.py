from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sorted_str = ""
            for c in sorted(s):
                sorted_str += c
            groups[sorted_str].append(s)
        
        res = []
        for sublist in groups.values():
            res.append(sublist)
        
        return res
        

