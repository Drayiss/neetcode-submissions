# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        size = e - s + 1
        if size <= 1:
            return

        m = s + (e - s) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)
        self.merge(pairs, s, m, e)

    def merge(self, pairs: List[Pair], s: int, m: int, e: int):
        sortedLeft = pairs[s : m + 1]
        sortedRight = pairs[m + 1 : e + 1]
        k = s
        l = 0
        r = 0

        while l < len(sortedLeft) and r < len(sortedRight):
            if sortedLeft[l].key <= sortedRight[r].key:
                pairs[k] = sortedLeft[l]
                l += 1
            else:
                pairs[k] = sortedRight[r]
                r += 1
            k += 1
        while l < len(sortedLeft):
            pairs[k] = sortedLeft[l]
            l += 1
            k += 1
        while r < len(sortedRight):
            pairs[k] = sortedRight[r]
            r += 1
            k += 1


