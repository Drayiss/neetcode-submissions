from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countsToStrs = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            
            countsToStrs[tuple(count)].append(s)
        
        return list(countsToStrs.values())
