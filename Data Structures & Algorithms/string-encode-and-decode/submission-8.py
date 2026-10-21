class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        i = 0

        while i < n:
            delimiter_index = i

            while s[delimiter_index] != "#":
                delimiter_index += 1

            word_len = int(s[i : delimiter_index])
            word_start = delimiter_index + 1
            word = s[word_start : word_start + word_len]

            res.append(word)

            i = word_start + word_len

        return res
            
                

            