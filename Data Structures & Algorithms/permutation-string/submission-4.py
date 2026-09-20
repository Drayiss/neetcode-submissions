class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord('a')
            s1_count[s1_index] += 1

            s2_index = ord(s2[i]) - ord('a')
            s2_count[s2_index] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        l = 0
        n = len(s2)
        for r in range(len(s1), n):
            if matches == 26:
                return True
            
            # Add s2[r]
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] + 1:
                matches -= 1

            # Remove s2[l]
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] - 1:
                matches -= 1

            l += 1
        
        return matches == 26
