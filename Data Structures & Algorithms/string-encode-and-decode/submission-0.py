class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            word_length = int(s[i : j])
            word_start_index = j + 1
            current_word = s[word_start_index : word_start_index + word_length]
            res.append(current_word)
            i = word_start_index + word_length

        return res

        