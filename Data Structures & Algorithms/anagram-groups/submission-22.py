from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_anagrams = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                normalized_value = ord(c) - ord('a')
                count[normalized_value] += 1
            count_to_anagrams[tuple(count)].append(s)

        res = []
        for sublist in count_to_anagrams.values():
            res.append(sublist)

        return res