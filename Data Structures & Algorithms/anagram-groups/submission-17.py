from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_sublist = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            
            count_to_sublist[tuple(count)].append(s)
        
        return [sublist for sublist in count_to_sublist.values()]