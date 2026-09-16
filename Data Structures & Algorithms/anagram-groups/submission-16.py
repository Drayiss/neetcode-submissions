from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_sublist = defaultdict(list)

        for s in strs:
            anagram_to_sublist[''.join(sorted(s))].append(s)

        return [sublist for sublist in anagram_to_sublist.values()]