from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list) # Map the charCounts to the list of matching strings

        for s in strs:
            counts = [0] * 26
            
            for c in s:
                counts[ord(c) - ord("a")] += 1

            counts_tuple = tuple(counts)
            my_dict[counts_tuple].append(s)

        return list(my_dict.values())