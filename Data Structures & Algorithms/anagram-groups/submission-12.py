from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_str_list = sorted(s)
            key = tuple(sorted_str_list)
                
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        res = []
        for sublist in groups.values():
            res.append(sublist)
        
        return res
        

