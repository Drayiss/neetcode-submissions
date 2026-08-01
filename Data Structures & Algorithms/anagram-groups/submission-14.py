from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            res_dict[key].append(s)
        
        return list(res_dict.values())
        

