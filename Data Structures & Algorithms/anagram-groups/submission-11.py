from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_str = ""
            for c in sorted(s):
                sorted_str += c
                
            if sorted_str not in groups:
                groups[sorted_str] = []
            groups[sorted_str].append(s)
        
        res = []
        for sublist in groups.values():
            res.append(sublist)
        
        return res
        

